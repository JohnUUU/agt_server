from abc import ABC
import time
from server import Server
import sys
import numpy as np
import pandas as pd


def determine_winner(action1, action2):
    if action1 == action2:
        return 3
    elif (action1 == 'rock' and action2 == 'scissors') or (action1 == 'paper' and action2 == 'rock') or (
            action1 == 'scissors' and action2 == 'paper'):
        return 0
    else:
        return 1


def get_utility(result):
    if result == 0:
        return [1, -1]
    elif result == 1:
        return [-1, 1]
    else:
        return [0, 0]


class RPSServer(Server, ABC):
    def __init__(self, n_players, n_rounds=100):
        super(RPSServer, self).__init__(n_players)
        self.pairings = None
        self.played = {p: set([]) for p in range(self.n_players)}
        self.players = list(range(n_players))
        self.n_rounds = n_rounds
        self.total_util = np.zeros([n_players, n_players])
        self.matches_played = {p: 0 for p in range(n_players)}

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
            matches += 1
            print(f'Pairings are {self.pairings}')
            # print(self.pairings)
            print(f'I am playing round {matches}')
            for r in range(self.n_rounds):
                # print(r)
                for match in self.pairings:
                    p0, p1 = match
                    if p1 is not None:
                        a0 = self.actions[p0][r + self.matches_played[p0]*self.n_rounds]
                        a1 = self.actions[p1][r + self.matches_played[p1]*self.n_rounds]
                        result = determine_winner(a0, a1)
                        # print(f'In round {r}, {a0} and {a1} were played by {p0} and {p1} to yield {result}')
                        u0, u1 = get_utility(result)
                        self.message[p0] = f'{[a1]}, {u0}'
                        self.message[p1] = f'{[a0]}, {u1}'
                        time.sleep(.001)
                        self.total_util[p0][p1] += u0
                        self.total_util[p1][p0] += u1
            for match in self.pairings:
                p0, p1 = match
                if p1 is not None:
                    self.matches_played[p0] += 1
                    self.matches_played[p1] += 1
            for i in range(self.n_players):
                self.message[i] = 'New Game'
                time.sleep(.001)
            self.round_robin()
        self.in_progress = False
        for i in range(self.n_players):
            self.message[i] = 'Game Over'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Please only enter the number of agents and number of rounds')
        sys.exit()
    n = int(sys.argv[1])
    r = int(sys.argv[2])
    server = RPSServer(n, r)
    server.start()
    df = pd.DataFrame(server.total_util)
    df.columns = server.agent_names
    df.index = server.agent_names
    means = []
    wins = []
    for d in server.total_util:
        # print(d)
        means.append(sum(d) / (len(d) - 1))
        wins.append(len(np.where(d > 0)[0]))
    df['Mean Points'] = means
    df['Number of Matches Won'] = wins
    df.sort_values('Mean Points')
    df.to_csv('results.csv')
    print(df)
