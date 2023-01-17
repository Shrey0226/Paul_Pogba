import random

def play():
    user = input("Choose r for rock, s for scissors, p for paper\n")
    computer = random.choice(['r', 's', 'p'])
    print("you choose " + user)
    print("computer choose " + computer)
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'you won'
        
    return 'you lost'


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True   
a = play()
print(a)
