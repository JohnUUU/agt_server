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
        self.my_moves = np.array([])

        # ACTIONS
        self.actions = ['rock', 'paper', 'scissors']

        # NOTE: Changing this will only change your agent's perception of the utility and
        #       will not change the actual utility used in the game
        self.utility = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])

    @staticmethod
    def softmax(x):
        return np.exp(x)/np.sum(np.exp(x))

    def get_action(self):
        move_p = self.calc_move_probs()
        my_move = np.random.choice(['rock', 'paper', 'scissors'], p=move_p)
        np.append(self.my_moves, my_move)
        return my_move

    def update(self, a_other, utility):
        """
        HINT: Update your move history and utility history to help find your best move in calc_move_probs
        """
        a_other = a_other[0]
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.opp_action_history.append(move_decode[a_other])

    def calc_move_probs(self):
        """
         Uses your historical average rewards to generate a probability distribution over your next move using 
         the Exponential Weights strategy

         HINT: np.random.choice might be useful

         Please return an array of ['rock', 'paper', 'scissors']
        """
        # TODO Write this
        raise NotImplementedError


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
        agent.update(opponent_action, util)
    print(f'After 1000 rounds, my score is {score}')
