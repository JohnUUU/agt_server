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
        self.actions = {i: [None]*1000000 for i in range(n_players)}
        self.wins = {i: 0 for i in range(n_players)}
        self.wins[3] = 0
        self.clients = defaultdict(lambda: None)
        self.in_progress = True
        self.message = {p: None for p in range(n_players)}

    def get_initial_message(self):
        raise NotImplementedError

    def run_game(self):
        raise NotImplementedError

    def create_pairings(self):
        raise NotImplementedError

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
            time.sleep(.002)

            initial_message = self.get_initial_message()
            client.send(initial_message.encode())
            self.clients[i] = client
            # Start the thread
            threading.Thread(target=self.handle_client, args=(client, i)).start()
        print(f'I have {self.n_players} agents connected and I am starting the game')
        self.run_game()

    # def handle_client(self, client, player_num):
    #     rounds_played = 0
    #     if player_num == 0:
    #         opp = 1
    #     else:
    #         opp = 0
    #     time.sleep(.002)
    #     while rounds_played < 5:
    #         # Wait for the agent to send its action
    #         self.actions[player_num][rounds_played] = client.recv(1024).decode()
    #         # Check if both agents have sent their actions
    #         while True:
    #             if self.actions[0][rounds_played] is not None and self.actions[1][rounds_played] is not None:
    #                 a1 = self.actions[0][rounds_played]
    #                 a2 = self.actions[1][rounds_played]
    #                 winner = determine_winner(a1, a2)
    #                 if winner == player_num:
    #                     util = 1.
    #                 elif winner == 3:
    #                     util = 0.
    #                 else:
    #                     util = -1.
    #                 if player_num == 0:
    #                     # print(f'It is round {rounds_played}. Player 0 played {a1} and player 1 played {a2}.')
    #                     self.wins[winner] += 1
    #                 client.send(f'{[self.actions[opp][rounds_played]]}, {util}'.encode())
    #                 rounds_played += 1
    #                 break
    #     client.send('Game Over'.encode())
    #     if player_num == 0:
    #         print(f'Player 0 won {self.wins[0]} times, player 1 won {self.wins[1]} time, '
    #               f'and there was {self.wins[3]} draws')
    #
    #     client.close()
    def handle_client(self, client, player_num):
        rounds_played = 0
        while self.in_progress:
            # Wait for the agent to send its action
            self.actions[player_num][rounds_played] = client.recv(1024).decode()
            rounds_played += 1
            while self.message[player_num] is None:
                pass
            client.send(self.message[player_num].encode())
            self.message[player_num] = None
        # client.send("Game Over".encode())
        client.close()