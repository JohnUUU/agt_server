import socket
import threading
import time
from collections import defaultdict


def determine_winner(action1, action2):
    if action1 == action2:
        return 3
    elif (action1 == 'rock' and action2 == 'scissors') or (action1 == 'paper' and action2 == 'rock') or (
            action1 == 'scissors' and action2 == 'paper'):
        return 0
    else:
        return 1


class Server:
    def __init__(self, n_players):
        self.n_players = n_players
        self.actions = {i: [None]*1000 for i in range(n_players)}
        self.wins = {i: 0 for i in range(n_players)}
        self.wins[3] = 0
        self.clients = defaultdict(lambda: None)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        # server.bind(('localhost', 1234))
        server.bind((IPAddr, 1234))
        print(f'The server is hosted at {IPAddr} and port 1234')
        server.listen()
        for i in range(self.n_players):
            client, address = server.accept()
            name = client.recv(1024).decode()
            print(f'Player {i} connected from {address} named {name}')
            # Send what player number they are
            client.send(str(i).encode())
            time.sleep(0.2)
            # Send an initial message, in this case it is the game we are playing. It can be a valuation or something instead
            client.send('RPS'.encode())
            self.clients[i] = client
            # Start the thread
            threading.Thread(target=self.handle_client, args=(client, i)).start()
        print('I have 2 agents connected')

    def handle_client(self, client, player_num):
        rounds_played = 0
        if player_num == 0:
            opp = 1
        else:
            opp = 0
        while rounds_played < 5:
            time.sleep(.2)
            # Wait for the agent to send its action
            self.actions[player_num][rounds_played] = client.recv(1024).decode()
            # Check if both agents have sent their actions
            while True:
                if self.actions[0][rounds_played] is not None and self.actions[1][rounds_played] is not None:
                    a1 = self.actions[0][rounds_played]
                    a2 = self.actions[1][rounds_played]
                    winner = determine_winner(a1, a2)
                    if winner == player_num:
                        util = 1.
                    elif winner == 3:
                        util = 0.
                    else:
                        util = -1.
                    if player_num == 0:
                        print(f'It is round {rounds_played}. Player 0 played {a1} and player 1 played {a2}.')
                        self.wins[winner] += 1
                    client.send(f'{[self.actions[opp][rounds_played]]}, {util}'.encode())
                    rounds_played += 1
                    break
        client.send('Game Over'.encode())
        if player_num == 0:
            print(f'Player 0 won {self.wins[0]} times, player 1 won {self.wins[1]} time, '
                  f'and there was {self.wins[3]} draws')

        client.close()


server = Server(2)
server.start()
