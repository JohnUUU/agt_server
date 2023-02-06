import sys
sys.path.append('../..')
sys.path.append('..')

from agent import Agent
import random



class BoSAgent(Agent):
    def setup(self):
        # ACTIONS
        self.current_state = 0
        # self.row_player = bool(random.getrandbits(1))
        self.row_player = ...
        self.threshold = 0.5
        self.good_mood = random.random() > self.threshold
        self.my_last_move = None
        self.col_player_mood = ...
        self.game_history = []

    def get_action(self):
        best_move = self.next_move()
        self.my_last_move = best_move
        return best_move

    def get_opp_utility(self, my_move, opp_move):
        if self.row_player:
            return self.col_player_reward_from(my_move, opp_move)
        else:
            return self.row_player_reward_from(my_move, opp_move)

    def update(self, a_other, utility):
        """
        Records the opponent move and calls transision state based on that move
        """
        self.game_history.append(
            {
                'my_move': self.my_last_move,
                'opp_move': a_other,
                'col_player_mood': self.col_player_mood,
                'utility': utility,
                'opp_reward': self.get_opp_utility(self.my_last_move, a_other)
            }
        )

    def next_move(self):
        """
        Return either 'S'(representing STUBBORN) or 'C' (representing COMPROMISE) based on the current state of the 
        game, as stored in the instance variable this.currentState. Note that this.currentState is initialized to 0, 
        which represents your initial state.
        """
        raise NotImplementedError

    def is_row_player(self):
        return self.row_player

    def get_mood(self):
        if self.row_player:
            return None
        elif self.good_mood:
            return "GOOD_MOOD"
        else:
            return "BAD_MOOD"

    def get_game_history(self):
        return self.game_history

    def column_player_good_mood_probability(self):
        return self.threshold
    
    def row_player_reward_from(self, my_move, opp_move): 
        if my_move == 'S' and opp_move == 'S':
            return 0
        elif my_move == 'S' and opp_move == 'C':
            return 7
        elif my_move == 'C' and opp_move == 'S':
            return 3
        else:
            return 0
    
    def col_player_reward_from(self, my_move, opp_move): 
        if self.col_player_mood:
            if my_move == 'S' and opp_move == 'S':
                return 0
            elif my_move == 'S' and opp_move == 'C':
                return 3
            elif my_move == 'C' and opp_move == 'S':
                return 7
            else:
                return 0
        else:
            if my_move == 'S' and opp_move == 'S':
                return 7
            elif my_move == 'S' and opp_move == 'C':
                return 0
            elif my_move == 'C' and opp_move == 'S':
                return 0
            else:
                return 3