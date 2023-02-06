def determine_winner(action1, action2):
    if action1 == action2:
        return 3
    elif (action1 == 'rock' and action2 == 'scissors') or (action1 == 'paper' and action2 == 'rock') or (
            action1 == 'scissors' and action2 == 'paper'):
        return 0
    else:
        return 1


def get_utility(result):
    if result == 0:
        return [1, -1]
    elif result == 1:
        return [-1, 1]
    else:
        return [0, 0]


# Legal actions for the game
actions = ['rock', 'paper', 'scissors']
