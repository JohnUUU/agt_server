from agent import Agent


class WMAgent(Agent):
    def __init__(self, name):
        super(WMAgent, self).__init__(name)
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return "This is an invalid move"

    def update(self, a_other, utility):
        return None


agent = WMAgent('Wrong Move Agent')
agent.connect()
