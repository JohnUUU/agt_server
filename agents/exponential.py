import numpy as np
from agent import Agent


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


agent = ExponentialAgent('Exponential Agent')
agent.connect()
