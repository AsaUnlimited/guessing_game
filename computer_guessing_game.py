import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guessed = random.randint(low, high)
        else:
            computer_guessed = low
        feedback = input(f"If {computer_guessed} too high (H), too low (L), or correct (C)??".lower())
        if feedback == 'h':
            high = computer_guessed - 1
        elif feedback == 'l':
            low = computer_guessed + 1
    print(f"The computer guessed my number {computer_guessed} correctly")
