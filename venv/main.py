#get random num
#get input
#check answer

from random import randint

answer = randint(1,10)
print(answer)

while True:
    try:
        guess = int(input("tell me a num in betw 1~10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("congrats")
                break
        else:
            print("hey bro, 1 ~ 10 pls")
    except ValueError:
        print("please try again with a number")
        continue