from abc import ABC
import time
from server import Server


def determine_winner(action1, action2):
    if action1 == action2:
        return 3
    elif (action1 == 'rock' and action2 == 'scissors') or (action1 == 'paper' and action2 == 'rock') or (
            action1 == 'scissors' and action2 == 'paper'):
        return 0
    else:
        return 1


class RPSServer(Server, ABC):
    def __init__(self, n_players, n_rounds=100):
        super(RPSServer, self).__init__(n_players)
        self.pairings = None
        self.played = {p: set([]) for p in range(self.n_players)}
        self.players = list(range(n_players))
        self.n_rounds = n_rounds

    def get_initial_message(self):
        return 'RPS'

    def round_robin(self):
        active_players = set([])
        self.pairings = []
        for p in self.players:
            if p not in active_players:
                for o in self.players:
                    if o != p and o not in active_players and o not in self.played[p]:
                        self.played[p].add(o)
                        self.played[o].add(p)
                        active_players.add(p)
                        active_players.add(o)
                        self.pairings.append([p, o])
                        break

    def run_game(self):
        self.round_robin()
        matches = 0
        while self.pairings:
            for r in range(self.n_rounds):
                for match in self.pairings:
                    p0, p1 = match
                    a0 = self.actions[p0][r + matches*self.n_rounds]
                    a1 = self.actions[p1][r + matches*self.n_rounds]
                    result = determine_winner(a0, a1)
                    print(f'In round {r}, {a0} and {a1} were played by {p0} and {p1} to yield {result}')
                    if result == 0:
                        u0 = 1
                        u1 = -1
                    if result == 1:
                        u1 = 1
                        u0 = -1
                    if result == 3:
                        u1 = 0
                        u0 = 0
                    self.message[p0] = f'{[a1]}, {u0}'
                    self.message[p1] = f'{[a0]}, {u1}'
                    time.sleep(.1)
            matches += 1
            self.round_robin()
        self.in_progress = False
        for i in range(self.n_players):
            self.message[i] = 'Game Over'


server = RPSServer(3, 1)
server.start()
