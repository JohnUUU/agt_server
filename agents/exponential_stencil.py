import numpy as np
from agent import Agent
import sys


class ExponentialAgent(Agent):
    def __init__(self, name):
        super(ExponentialAgent, self).__init__(name)
        self.setup()

    def setup(self):
        self.my_moves = np.array([])

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
        my_move = self.calcMoveProbabilities()
        np.append(self.my_moves, my_move)
        return my_move

    def update(self, a_other, utility):
        """
        HINT: Update your move history and utility history to help find your best move in calcMoveProbabilities
        """
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        raise NotImplementedError

    def calcMoveProbabilities(self):
        """
         Uses your historical average rewards to generate a probability distribution over your next move using 
         the Exponential Weights strategy

         HINT: np.random.choice might be useful

         Please return your best move (one of [self.ROCK, self.PAPER, self.SCISSOR])
        """
        raise NotImplementedError

# agent = ExponentialAgent('Exponential Agent')
# agent.connect()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = ExponentialAgent(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
