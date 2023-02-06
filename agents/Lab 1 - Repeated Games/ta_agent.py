import random
from agent import Agent
import sys


class TAAgent(Agent):
    def setup(self):
        self.history = []
        self.actions = ['rock', 'paper']

    def get_action(self):
        return random.choice(self.actions)

    def update(self, a_other, utility):
        return None
