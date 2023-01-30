import random
from agent import Agent
import sys
from ta_agent import TAAgent
from utils import determine_winner


class CompAgent(Agent):
    def setup(self):
        # TODO If you use any new objects in the class for update and get_action, please initialize them here
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        # TODO return what action to play next from self.actions
        raise NotImplementedError

    def update(self, a_other, utility):
        # TODO Choose how to use the information you get from the simulator to make your next move
        # a_other is a list of length 1 containing the opponent's action
        raise NotImplementedError


if __name__ == "__main__":
    # TODO Edit this to match the IP given by the TAs and name your agent for the leaderboard
    ip = '10.38.0.36'
    port = 1234
    name = "MyAgentName"
    test = True

    if not test:
        agent = CompAgent(name)
        agent.connect(ip=ip, port=port)
    else:
        agent = CompAgent('My Agent')
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
