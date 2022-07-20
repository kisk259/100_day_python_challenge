import random

from art import logo, vs
from game_data import data


def choose_random_person():
    person = data[random.randint(0, len(data) - 1)]
    return person


def compare(person_1, person_2):
    p1_follower_count = person_1['follower_count']
    p2_follower_count = person_2['follower_count']

    if p1_follower_count > p2_follower_count:
        return "A"
    elif p1_follower_count < p2_follower_count:
        return "B"

def printing(p):
    return print(f"Compare A: {p['name']}, a {p['description']}, from {p['country']}")

def game():
    run_game = True
    print(logo)
    while run_game:
        p1 = choose_random_person()
        p2 = choose_random_person()
        if p1 == p2:
            p2 = choose_random_person()
        printing(p1)
        print(vs)
        printing(p2)
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if compare(p1, p2) == "p1":


game()