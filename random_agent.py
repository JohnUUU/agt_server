import socket
import random
from agent import Agent


class RandomAgent(Agent):
    def __init__(self, name):
        super(RandomAgent, self).__init__(name)
        self.history = []

    def get_action(self):
        action = random.choice(['rock', 'paper', 'scissors'])
        return action

    def update(self, a_other, utility):
        return None


agent = RandomAgent('Agent 1')
agent.connect(ip='localhost', port=1234)
