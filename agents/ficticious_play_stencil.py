import numpy as np
from agent import Agent
import sys


class FicticiousPlayAgent(Agent):
    def setup(self):
        self.opp_action_history = []

        # ACTIONS
        self.ROCK, self.PAPER, self.SCISSOR = 0, 1, 2
        self.actions = ['rock', 'paper', 'scissors']

        # NOTE: Changing this will only change your perception of the utility and will not
        #       change the actual utility used in the game
        self.utility = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])

    def get_action(self):
        dist = self.predict()
        best_move = self.optimize(dist)
        return self.actions[best_move]

    def update(self, a_other, utility):
        """
        Updates opp action history to be a record of opponent moves 
            Rock - 0, Paper - 1, Scissors - 2
        """
        a_other = a_other[0]
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.opp_action_history.append(move_decode[a_other])

    def predict(self):
        """
        Uses the opponent’s previous moves (self.opp_action_history) to generate and save a probability distribution 
        over the opponent’s next move in (self.dist).
        """
        raise NotImplementedError

    def optimize(self, dist):
        """
        Given the distribution over the opponent's next move (output of predict) and knowledge of the payoffs (self.utility),
        Return the best move according to Ficticious Play. 
        Please return one of [self.ROCK, self.PAPER, self.SCISSORS]
        """
        raise NotImplementedError


# agent = FicticiousPlayAgent('Ficticious Play')
# # agent.connect()
# agent.connect(ip='10.38.33.90', port=1234)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = FicticiousPlayAgent(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
