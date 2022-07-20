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
        return False
    elif p1_follower_count < p2_follower_count:
        return True


def game():
    run_game = True
    while run_game:
        p1 = choose_random_person()
        p2 = choose_random_person()
        if p1 == p2:
            p2 = choose_random_person()
        print(logo)
        print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}")
        print(vs)
        print(f"Compare A: {p2['name']}, a {p2['description']}, from {p2['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        compare(p1, p2)
