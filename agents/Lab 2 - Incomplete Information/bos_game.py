def get_utility(a0, a1):
    if a0 == 'S' and a1 == 'S':
        return [0, 0]
    if a0 == 'S' and a1 == 'C':
        return [7, 3]
    if a0 == 'C' and a1 == 'S':
        return [3, 7]
    if a0 == 'C' and a1 == 'C':
        return [0, 0]
    if a0 in ['C', 'S']:
        return [7, 0]
    else:
        return [0, 7]


# Legal actions for the game
actions = ['S', 'C']
