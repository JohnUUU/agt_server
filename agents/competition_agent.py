import random
from agent import Agent
import sys
from ta_agent import TAAgent
from game import *


class CompAgent(Agent):
    def setup(self):
        self.history = []
        self.actions = actions

    def get_action(self):
        return random.choice(self.actions)

    def update(self, a_other, utility):
        return None


if __name__ == "__main__":
    # TODO Edit this to match the IP given by the TAs and name your agent for the leaderboard
    ip = '10.38.61.72'
    port = 1234
    name = "MyAgentName"
    test = False

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
            util = get_utility(result)[0]
            score += util
            agent.update([opponent_action], util)
        print(f'After 1000 rounds, my score is {score}')
