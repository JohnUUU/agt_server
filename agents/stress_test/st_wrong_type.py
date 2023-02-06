from agent import Agent
import sys


class WTAgent(Agent):
    def setup(self):
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return -1

    def update(self, a_other, utility):
        return None


# agent = WMAgent('Wrong Move Agent')
# agent.connect()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = WTAgent(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
