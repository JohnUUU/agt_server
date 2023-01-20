import socket
import random
from agent import Agent


class RandomAgent(Agent):
    def __init__(self, name):
        super(RandomAgent, self).__init__(name)

    def get_action(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def update(self, a_other, utility):
        return None


agent = RandomAgent('Agent 1')
agent.connect(ip='10.38.33.90', port=1234)
