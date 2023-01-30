import random
import numpy as np
from agent import Agent
from ta_agent import TAAgent
from utils import determine_winner
import sys


class ExponentialAgent(Agent):
    def __init__(self, name):
        super(ExponentialAgent, self).__init__(name)
        self.setup()

    def setup(self):
        self.tot_utility = np.array([0.0, 0.0, 0.0])
        self.move_count = np.array([0, 0, 0])
        self.my_move = None

        # ACTIONS
        self.ROCK, self.PAPER, self.SCISSOR = 0, 1, 2
        self.actions = ['rock', 'paper', 'scissors']

        # NOTE: Changing this will only change your agent's perception of the utility and
        #       will not change the actual utility used in the game
        self.utility = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])

    @staticmethod
    def softmax(x):
        return np.exp(x)/np.sum(np.exp(x))

    def get_action(self):
        self.my_move = self.find_best_move()
        return self.my_move

    def update(self, a_other, utility):
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.tot_utility[move_decode[self.my_move]] += float(utility)
        self.move_count[move_decode[self.my_move]] += 1

    def find_best_move(self):
        avg_utility = self.tot_utility / \
            np.maximum(np.ones(3), self.move_count)
        return np.random.choice(self.actions, p=self.softmax(avg_utility))


# agent = ExponentialAgent('Exponential Agent')
# agent.connect()

if __name__ == "__main__":
    agent = ExponentialAgent('My Agent')
    opponent = TAAgent('TAAgent')
    score = 0
    for _ in range(1000):
        my_action = agent.get_action()
        opponent_action = opponent.get_action()
        result = determine_winner(my_action, opponent_action)
        if result == 0:
            util = 1
            score += 1
        elif result == 1:
            util = -1
            score -= 1
        else:
            util = 0
        agent.update([opponent_action], util)
    print(f'After 1000 rounds, my score is {score}')
