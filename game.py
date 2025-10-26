import random

def roll_two_d6():
    d1 = random.randint(1,6)
    d2= random.randint(1, 6)
    if d1 == d2:
        roll_two_d6()
    return d1,d2

def d_score(roll):
    return sum(roll)


def tie_breaker():
    while True:
        s1 = d_score(roll_two_d6())
        s2 = d_score(roll_two_d6())
        if s1 == s2:
            continue
        elif s1 > s2:
            return 1
        else:
            return 2
def turn_decision():
    while True:
        choice = input("Roll or Pass: r to roll p to pass ").lower()
        if choice not in ["r","p"]:
            continue
        return choice

def play_game():
    pass_count = 0
    sc_p1 = 0
    sc_p2 = 0
    while True:
        choice_p1= turn_decision()
        if choice_p1 == "r":
            pass_count = 0
            player_1 = roll_two_d6()
            sc_p1 += d_score(player_1)
            if is_exact_100(sc_p1):
                print("PLAYER 1 WON !!!")
                break
            elif is_bust(sc_p1):
                print("PLAYER 2 WON !!!")
                break
            else:
                print(f"Player 1: Roll:{player_1} , Score:{sc_p1}")

        else:
            pass_count += 1
            if pass_count == 2:
                if sc_p1 != sc_p2:
                    return closer_to_target(sc_p1,sc_p2)
                else:
                    return tie_breaker()

        choice_p2 = turn_decision()
        if choice_p2 == "r":
            pass_count = 0
            player_2 = roll_two_d6()
            sc_p2 += d_score(player_2)
            if is_exact_100(sc_p2):
                print("PLAYER 2 WON !!!")
                break
            elif is_bust(sc_p2):
                print("PLAYER 2 WON !!!")
                break
            else:
                print(f"Player 2: Roll:{player_2} , Score:{sc_p2}")
        else:
            pass_count += 1
            if pass_count == 2:
                if sc_p2 != sc_p1:
                    return closer_to_target(sc_p1, sc_p2)
                else:
                    return tie_breaker()
        continue

























