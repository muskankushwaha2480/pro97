import random


number = random.randint(1,9)
chances = 0

while chances < 5:
    guess = int(input("Guess the number : "))
    chances= chances +  1
    if guess == number:
        print("Congratulations!! YOU WON!!")
        break
    elif guess>number :
        print("Very Close!! Guess a little small no. ")
    
    else:
        print("Very close!! Guess a little high no.")
    

if not chances < 5 :
    print("You Lose! ")
    print("The number was : ")
    print(number)


