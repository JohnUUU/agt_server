import numpy as np
from agent import Agent


class FicticiousPlayAgent(Agent):
    def __init__(self, name):
        super(FicticiousPlayAgent, self).__init__(name)
        self.action_history = []

        # ACTIONS
        self.ROCK, self.PAPER, self.SCISSOR = 0, 1, 2
        self.actions = ['rock', 'paper', 'scissors']

        # NOTE: Changing this will only change your perception of the utility and will not
        #       change the actual utility used in the game
        self.utility = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
        self.dist = np.array([0, 0, 0])
        self.payoffs = np.array([0, 0, 0])

    def get_action(self):
        self.predict()
        best_move = self.optimize()
        return self.actions[best_move]

    def update(self, a_other, utility):
        a_other = a_other[0]
        move_decode = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.action_history.append(move_decode[a_other])

    def predict(self):
        self.dist = np.array([0, 0, 0])
        for action in self.action_history:
            self.dist[action] += 1
        total = np.sum(self.dist)
        if total > 0:
            self.dist = self.dist / total

    def optimize(self):
        for action in range(len(self.payoffs)):
            self.payoffs[action] += np.sum(self.dist * self.utility[action])
        best_move = np.argmax(self.payoffs)
        return best_move


agent = FicticiousPlayAgent('Ficticious Play')
agent.connect()
# agent.connect(ip='10.38.33.90', port=1234)
