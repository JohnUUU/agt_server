from agent import Agent


class RandomAgent(Agent):
    def __init__(self, name):
        super(RandomAgent, self).__init__(name)
        self.history = []
        self.actions = ['rock', 'paper', 'scissors']

    def get_action(self):
        return 'rock'

    def update(self, a_other, utility):
        return None


agent = RandomAgent('Agent 1')
# agent.connect()
agent.connect(ip='10.38.33.90', port=1234)
