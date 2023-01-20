import socket
import random


class Agent:
    def __init__(self, name):
        self.name = name
        self.client = None

    def connect(self, ip='localhost', port=1234):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 1234))
        self.client.send(self.name.encode())
        player_num = int(self.client.recv(1024).decode())
        print(f'I am player {player_num}')
        self.play()

    def get_action(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def update(self, a_other, utility):
        return None

    def play(self):
        self.game = self.client.recv(1024).decode()
        print(f'We are playing {self.game}')
        while True:
            action = self.get_action()
            self.client.send(action.encode())
            print(f'I played {action}')
            response = self.client.recv(1024).decode()
            print(f'The response is {response}')
            if response == 'Game Over':
                break
            opp_action, util = response.strip().split(',')
            print(f'My opponent played {opp_action} and I got {util} utility')
            self.update(opp_action, util)
        self.close()

    def close(self):
        self.client.close()


agent = Agent('Agent 1')
agent.connect()
