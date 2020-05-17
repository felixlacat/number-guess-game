import random
import time
tries = 3 # the number of tries a player has
chossen = random.randint(1,10)# number generator
while True:
    print("pick a number between 1 and 10")# ask player to put their guess
    guess = input()
    if int(guess) == int(chossen):# if  your guess it right you win
        print("yay! you won")
        time.sleep(10)
        break
    elif int(guess) != int(chossen):
        tries = tries - 1 # subtracts their tries
        if int(tries == 0):# if you have no more tries you lose
            print("Sorry you lost")
            time.sleep(10)# wati 10 seconds
            break
        print("try again. you have " + str(tries) + " more tries \n")# tells player tries left
        if int(guess) < int(chossen): print("the number is greater \n")#tells player if the number is greater or less than what they chose
        elif int(guess) > int(chossen): print("the number is less \n")
#when you learn how to make add music and add animations do so because i have a
#vission of cconfetty and celebration when you get it right and
#bad sounds when you fail
