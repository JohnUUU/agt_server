import numpy as np
from agent import Agent
from ta_agent import TAAgent
from rps_game import *


class FictitiousPlayAgent(Agent):
    def setup(self):
        self.opp_action_history = []

        # ACTIONS
        self.actions = actions

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
        dist = np.zeros(len(self.actions))
        for a in self.opp_action_history:
            dist[a] += 1
        if sum(dist) == 0:
            return np.ones(len(self.actions))/len(self.actions)
        return dist/sum(dist)

    def optimize(self, dist):
        """
        Given the distribution over the opponent's next move (output of predict) and knowledge of the payoffs (self.utility),
        Return the best move according to Ficticious Play.
        Please return one of ['rock', 'paper', 'scissors']
        """
        # TODO Calculate the expected payoff of each action and return the action with the highest payoff
        action_utils = np.zeros(len(self.actions))
        for i, a in enumerate(self.actions):
            # Calculate the payoff
            for j, a in enumerate(self.actions):
                action_utils[i] += dist[j]*self.utility[i][j]

        best_action = np.argmax(action_utils)
        return best_action


if __name__ == "__main__":
    agent = FictitiousPlayAgent('My Agent')
    opponent = TAAgent('TAAgent')
    score = 0
    for _ in range(1000):
        my_action = agent.get_action()
        opponent_action = opponent.get_action()
        result = determine_winner(my_action, opponent_action)
        util = get_utility(result)[0]
        score += util
        agent.update([opponent_action], util)
    print(f'After 1000 rounds, my score is {score}')
