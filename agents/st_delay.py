from agent import Agent
import time


class Thinker(Agent):
    def __init__(self, name):
        super(Thinker, self).__init__(name)
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        time.sleep(10000)
        return 'rock'

    def update(self, a_other, utility):
        return None


agent = Thinker('Thinking Agent')
agent.connect()
