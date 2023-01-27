import socket
import ast


class Agent:
    def __init__(self, name):
        self.name = name
        self.client = None
        self.first_message = None
        self.player_num = None
        self.first_game = True
        self.setup()

    def setup(self):
        raise NotImplementedError

    def restart(self):
        self.first_game = False
        self.setup()

    def connect(self, ip='localhost', port=1234):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        self.client.send(self.name.encode())
        player_num = int(self.client.recv(1024).decode())
        self.player_num = player_num
        print(f'I am player {player_num}')
        self.play()

    def get_action(self):
        raise NotImplementedError

    def update(self, a_other, utility):
        raise NotImplementedError

    def play(self):
        self.first_message = self.client.recv(1024).decode()
        print(f'We are playing {self.first_message}')
        while True:
            action = self.get_action()
            # print(f'I played {action}')
            self.client.send(action.encode())
            response = self.client.recv(1024).decode()
            if response == 'Game Over':
                print(f'I am agent {self.player_num} and my game is over')
                break
            elif response == 'New Game':
                self.setup()
            else:
                opp_action, util = response.strip().split(',')
                opp_action = ast.literal_eval(opp_action)
                self.update(opp_action, util)
        self.close()

    def close(self):
        self.client.close()
