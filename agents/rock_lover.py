from agent import Agent


class RockLovingAgent(Agent):
    def __init__(self, name):
        super(RockLovingAgent, self).__init__(name)
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return 'rock'

    def update(self, a_other, utility):
        return None


agent = RockLovingAgent('Rock Loving Agent')
agent.connect()
#agent.connect(ip='10.38.33.90', port=1234)
