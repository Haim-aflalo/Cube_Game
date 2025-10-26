
def  is_bust(score):
    return score > 100

def is_exact_100(score: int):
    return score == 100

def closer_to_target(a: int, b: int):
    if a > b:
        return 1
    if b > a:
        return 2

