from agent import Agent
import sys


class RockLovingAgent(Agent):
    def setup(self):
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return 'rock'

    def update(self, a_other, utility):
        return None


# agent = RockLovingAgent('Rock Loving Agent')
# agent.connect()
# #agent.connect(ip='10.38.33.90', port=1234)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = RockLovingAgent(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
