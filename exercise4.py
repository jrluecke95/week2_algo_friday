import random

def magicBall():
    question = input("What is your question? ")
    num = random.randint(1, 3)
    if num == 1:
        print("yes")
    if num == 2:
        print("no")
    if num == 3:
        print("maybe")


magicBall()
