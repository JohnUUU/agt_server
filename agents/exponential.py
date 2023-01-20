import numpy as np
from agent import Agent


class ExponentialAgent(Agent):
    def __init__(self, name):
        super(ExponentialAgent, self).__init__(name)
        self.tot_utility = np.array([0.0, 0.0, 0.0])
        self.move_count = np.array([0, 0, 0])

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
        best_move = self.find_best_move()
        return self.actions[best_move]

    def update(self, a_other, utility):
        a_other = a_other[0]
        print(utility)
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.tot_utility[move_decode[a_other]] += float(utility)
        self.move_count += 1

    def find_best_move(self):
        avg_utility = self.tot_utility / \
            np.maximum(np.ones(3), self.move_count)
        return np.argmax(self.softmax(avg_utility))


agent = ExponentialAgent('Agent 1')
agent.connect()
