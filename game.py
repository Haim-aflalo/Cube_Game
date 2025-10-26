import random
def roll_two_d6():
    d1 = random.randint(1,6)
    d2= random.randint(1, 6)
    return d1,d2

def d_score(roll):
    return sum(roll)

def  is_bust(score):
    return score > 100


def is_exact_100(score: int):
    return score == 100

def closer_to_target(a: int, b: int):
    if a > b:
        return 1
    if b > a:
        return 2
    return None

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
        choice = input("Roll or Pass: r to roll p to pass").lower()
        if choice not in ["r","p"]:
            continue
        return choice

def play_game():
    while True:
        count_sc_p1 = 0
        count_sc_p2 = 0
        player_1 = roll_two_d6()
        player_2 = roll_two_d6()
        score_p1 = d_score(player_1)
        count_sc_p1 += score_p1
        if is_bust(count_sc_p1):
            print("player2 WIN !!!")
            break
        score_p2 = d_score(player_2)
        count_sc_p2 += score_p2
        if is_bust(count_sc_p2):
            print("player1 WIN !!!")
            break
        if is_exact_100(count_sc_p1):
            print("PLAYER 1 WIN !!!")
            break
        if is_exact_100(count_sc_p2):
            print("PLAYER 2 WIN !!!")
            break
        else:
            print("score round p1:",score_p1,"score all games p1:",count_sc_p1)
            print("score round p2:",score_p2,"score all games p2:",count_sc_p2)
        p1_next = turn_decision()
        p2_next = turn_decision()
        if p1_next == "r" == p2_next:
            continue
        elif p1_next == "p" == p2_next:
            closer_to_target(count_sc_p1,count_sc_p2)
        elif p1_next == "r" and p2_next == "p":
            new_role_p1 = roll_two_d6()
            score_nr_p1 = d_score(new_role_p1)
            count_sc_p1 += score_nr_p1
            if is_bust(count_sc_p1):
                print("PLAYER 2 WIN !!!")
                break
            elif is_exact_100(count_sc_p1):
                print("PLAYER 1 WIN !!!")
                break
            continue
        elif p1_next == "p" and p2_next == "r":
            new_role_p2 = roll_two_d6()
            score_nr_p2 = d_score(new_role_p2)
            count_sc_p2 += score_nr_p2
            if is_bust(count_sc_p2):
                print("PLAYER 1 WIN !!!")
                break
            elif is_exact_100(count_sc_p2):
                print("PLAYER 2 WIN !!!")
                break
            continue


print(play_game())