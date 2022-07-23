import random
from replit import clear
from art import logo, vs
from game_data import data


def choose_random_person():
    person = random.choice(data)
    return person


def printing(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"


def compare(person_1, person_2, guess):
    p1_follower_count = person_1['follower_count']
    p2_follower_count = person_2['follower_count']

    if p1_follower_count > p2_follower_count:
        return guess == "A"
    else:
        return guess == "B"


def game():
    rounds = 0
    run_game = True
    print(logo)
    p1 = choose_random_person()
    p2 = choose_random_person()

    while run_game:
        p1 = p2
        p2 = choose_random_person()
        while p1 == p2:
            p2 = choose_random_person()

        print(f"Compare A: {printing(p1)}")
        print(vs)
        print(f"Against B: {printing(p2)}")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        clear()
        print(logo)

        if compare(p1, p2, answer):
            rounds += 1
            print(f"You're right! Current score: {rounds}")
        else:
            print(f"Sorry, that's wrong. Final score: {rounds}")
            run_game = False


game()
