import random

def secretNum():
    random_num = random.randint(1, 10)
    user_guess = int(input("Hey user! Can you guess the secret number?"))
    if user_guess == random_num:
        print(f"Correct! {random_num} was the number")
    else:
        while user_guess != random_num:
            print("wrong")
            user_guess = int(input("Try again "))
        print(f"Correct! {random_num} was the number")

secretNum()