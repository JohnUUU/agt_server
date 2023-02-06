import sys
sys.path.append('../..')
sys.path.append('..')

from bos_game import *
from agent import Agent
from bos_reluctant_agent import BoSReluctantAgent


class BoSCompetitionAgent(Agent):
    def setup(self):
        # ACTIONS
        self.actions = actions
        self.current_state = 0

    def get_action(self):
        best_move = self.next_move()
        return best_move

    def update(self, a_other, utility):
        """
        Records the opponent move and calls transision state based on that move
        """
        self.transistion_state(a_other[0])

    def next_move(self):
        """
        Return either 'S'(representing STUBBORN) or 'C' (representing COMPROMISE) based on the current state of the 
        game, as stored in the instance variable this.currentState. Note that this.currentState is initialized to 0, 
        which represents your initial state.
        """
        #TODO: Implement this section

    def transistion_state(self, opp_move):
        """
        This should, based on your current state, and the actions taken by each player in the previous round of the 
        game (which are derived from the game report received after each round), updates this.currentState to reflect
        the new state of the game.
        """
        #TODO: Implement this section


if __name__ == "__main__":
    # TODO Edit this to match the IP given by the TAs and name your agent for the leaderboard
    ip = '10.38.61.72'
    port = 1234
    name = "MyAgentName"
    test = False

    if not test:
        agent = BoSCompetitionAgent(name)
        agent.connect(ip=ip, port=port)
    else:
        agent = BoSCompetitionAgent('My Agent')
        opponent = BoSReluctantAgent('TAAgent')
        score = 0
        for _ in range(1000):
            my_action = agent.get_action()
            opponent_action = opponent.get_action()
            util = get_utility(my_action, opponent_action)[0]
            score += util
            agent.update([opponent_action], util)
        print(f'After 1000 rounds, my score is {score}')
