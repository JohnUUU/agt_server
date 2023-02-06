from agent import Agent
import time
import sys


class Thinker(Agent):
    def setup(self):
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        time.sleep(10000)
        return 'rock'

    def update(self, a_other, utility):
        return None


# agent = Thinker('Thinking Agent')
# agent.connect()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = Thinker(sys.argv[1])
    agent.connect(ip='10.38.0.36', port=1234)
