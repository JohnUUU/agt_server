import socket


class Agent:
    def __init__(self, name):
        self.name = name
        self.client = None
        self.first_message = None

    def connect(self, ip='localhost', port=1234):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        self.client.send(self.name.encode())
        player_num = int(self.client.recv(1024).decode())
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
            self.client.send(action.encode())
            response = self.client.recv(1024).decode()
            if response == 'Game Over':
                break
            elif response == 'New Game':
                self.__init__(self.name)
            else:
                opp_action, util = response.strip().split(',')
                self.update(opp_action, util)
        self.close()

    def close(self):
        self.client.close()
