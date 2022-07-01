import random


def guess(n):
    random_num = random.randint(1, n)
    player_guessed_num = 0
    while player_guessed_num != random_num:
        player_guessed_num = int(input(f"Guess a number between 1 and {n}: "))
        if player_guessed_num < random_num:
            print(f"Try again, you guess too low")
        elif player_guessed_num > random_num:
            print(f"Try again, you guess too high")
    print(f"Congrats, you guess right BOOM! {random_num}")