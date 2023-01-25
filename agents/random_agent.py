import random
from agent import Agent
import sys


class RandomAgent(Agent):
    def setup(self):
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return random.choice(self.actions)

    def update(self, a_other, utility):
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = RandomAgent(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
