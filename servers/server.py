import socket
import threading
import time
from collections import defaultdict


class Server:
    def __init__(self, n_players):
        self.n_players = n_players
        self.actions = {i: [None]*1000000 for i in range(n_players)}
        self.wins = {i: 0 for i in range(n_players)}
        self.wins[3] = 0
        self.clients = defaultdict(lambda: None)
        self.in_progress = True
        self.message = {p: None for p in range(n_players)}
        self.agent_names = [None]*n_players

    def get_initial_message(self):
        raise NotImplementedError

    def run_game(self):
        raise NotImplementedError

    def create_pairings(self):
        raise NotImplementedError

    def start(self):
        # Set up the server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        server.bind((IPAddr, 1234))
        print(f'The server is hosted at {IPAddr} and port 1234')
        server.listen()

        # Wait for the players to connect
        for i in range(self.n_players):
            client, address = server.accept()
            name = client.recv(1024).decode()
            print(f'Player {i} connected from {address} named {name}')
            self.agent_names[i] = name

            # Send what player number they are
            client.send(str(i).encode())
            time.sleep(.002)

            # Send the initial message
            initial_message = self.get_initial_message()
            client.send(initial_message.encode())
            self.clients[i] = client

            # Start the thread
            threading.Thread(target=self.handle_client, args=(client, i)).start()

        print(f'I have {self.n_players} agents connected and I am starting the game')
        self.run_game()

    def handle_client(self, client, player_num):
        """
        This is the command that runs on each thread. At each round something is added into self.actions and then a
        message is sent. The server in_progress flag determines when the game ends
        """
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
        time.sleep(.2)
        client.close()
