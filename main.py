# get random num
# get input
# check answer

from random import randint
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

answer = randint(int(num1), int(num2))

while True:
    try:
        guess = int(input(f"tell me a num in betw {num1}~{num2}:  "))
        if (int(num1) - 1) < guess < (int(num2) + 1):
            if guess < answer:
                print("guess a higher number")
            elif guess > answer:
                print("your guess too high")
            else:
                print("congrats")
                break
        else:
            print(f"hey bro, {num1} ~ {num2} pls")
    except ValueError:
        print("please try again with a number")
        continue
