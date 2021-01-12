import random

def play():
    user = input('''Choose 'r' for rock, 'p' for paper, 's' for scissors''')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return '''It's a Tie!'''
    
    if is_winner(user, computer):
        return '''You've won!'''

    return '''You've lost!'''

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
