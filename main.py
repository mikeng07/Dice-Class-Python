import player
import check_input




def take_turn(p):
    """roll dice to check if where a pair, series, or 3 of kind"""
    p.roll_dice()
    print(p)
    
    if (p.has_three_of_a_kind()):
        print("you got 3 of a kind")
    elif (p.has_pair()):
        print("you got a pair")
    elif (p.has_series()):
        print("you got a serires of 3!")
    else:
        print("Aww. Too bad.")

    print("Score = ", str(p.get_points()))

def main():
    p = player.Player()
    print ("-Yahtzee-")

    choice = True
    while choice:
        print()
        take_turn(p)
        choice = check_input.get_yes_no("Play again? (Y/N): ")

    print("Game Over.")
    print("Final Score = " + str(p.get_points()))


main() 
