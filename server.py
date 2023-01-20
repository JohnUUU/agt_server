import socket
import threading
import time
from collections import defaultdict

# A dictionary to store the actions of the agents
actions = {0: [None]*1000, 1: [None]*1000}


# A function to determine the winner of a round
def determine_winner(action1, action2):
    if action1 == action2:
        return 3
    elif (action1 == 'rock' and action2 == 'scissors') or (action1 == 'paper' and action2 == 'rock') or (
            action1 == 'scissors' and action2 == 'paper'):
        return 0
    else:
        return 1


# A function to handle a single client
def handle_client(client, player_num):
    rounds_played = 0
    if player_num == 0:
        opp = 1
    else:
        opp = 0
    while rounds_played < 5:
        time.sleep(.2)
        # Wait for the agent to send its action
        print(f'I am here for player {player_num}')
        actions[player_num][rounds_played] = client.recv(1024).decode()
        print(actions[player_num][rounds_played])
        # Check if both agents have sent their actions
        while True:
            if actions[0][rounds_played] is not None and actions[1][rounds_played] is not None:
                a1 = actions[0][rounds_played]
                a2 = actions[1][rounds_played]
                winner = determine_winner(a1, a2)
                print(f'The winner is {winner}')
                if winner == player_num:
                    util = 1
                elif winner == 3:
                    util = 0
                else:
                    util = -1
                if player_num == 0:
                    print(f'It is round {rounds_played}. Player 1 played {a1} and player 2 played {a2}. '
                      f'Player {winner} won')
                print(actions[opp][rounds_played], winner)
                client.send(f'{actions[opp][rounds_played]}, {util}'.encode())
                rounds_played += 1
                break
    print(f'game over for player {player_num}')
    client.send('Game Over'.encode())
    client.close()


# A dictionary to store the clients
clients = defaultdict(lambda: None)


# Create a socket to listen for incoming connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 1234))
server.listen()

# Wait for 2 agents to connect
for i in range(2):
    client, address = server.accept()
    name = client.recv(1024).decode()
    print(f'Player {i} connected from {address} named {name}')
    # Send what player number they are
    client.send(str(i).encode())
    time.sleep(0.2)
    # Send an initial message, in this case it is the game we are playing. It can be a valuation or something instead
    client.send('RPS'.encode())
    clients[i] = client
    # Start the thread
    threading.Thread(target=handle_client, args=(client, i)).start()
print('I have 2 agents connected')
