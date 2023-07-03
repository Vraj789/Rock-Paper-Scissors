from random import randint


def get_name():
    a= input("What is your name?")
    clear_screen()
    return a


def get_comp_num():
    return randint(1, 3)


def get_user_num(x):
    a= int(input(x + ", Choose 1 for Rock, 2 for Paper, 3 for Scissors"))
    clear_screen()
    return a


def display_moves(x,y, a, b):
    # x is players name, a is player's number b is comp num
    # this converts the numbers to 1=Rock 2=Paper and 3=Scissors
    if a == 1:
        print(x + " chose rock")
    if a == 2:
        print(x + " chose paper")
    if a == 3:
        print(x + " chose scissors")
    if b == 1:
        print(y+ " chose rock")
    if b == 2:
        print(y+ " chose paper")
    if b == 3:
        print(y +" chose scissors")


def check_winner(a,b, p, c):
    # p is players num c is computers num, this compares to see who wins and prints winner
    if p == c:
        print("There is a tie!")
    elif p == 1 and c == 2:
        print(b+" wins")
    elif p == 1 and c == 3:
        print(a + " wins")
    elif p == 2 and c == 3:
        print(b+ " wins")
    elif p == 2 and c == 1:
        print(a + " wins")
    elif p == 3 and c == 1:
        print(b+ " wins")
    elif p == 3 and c == 2:
        print(a + " wins")


def get_number_of_players():
    a= int(input("How many players do you want? 1 or 2?"))
    clear_screen()
    return a

def clear_screen():
    for i in range(0,9):
        print("")

# def check_play_again():

def main():
    numPlayers = get_number_of_players()
    if numPlayers == 1:
        playAgain = True
        name1 = get_name()
        name2 = "computer"
        while playAgain:
            player2Num = get_comp_num()
            player1Num = get_user_num(name1)
            display_moves(name1, name2, player1Num, player2Num)
            check_winner(name1, name2,player1Num, player2Num)


main()
