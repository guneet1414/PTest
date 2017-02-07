import random

print('Guess a number between 1-20')

secretNum = random.randint(1,6) #Picks a random number between 1 and 20


for tries in range (1,6):
    Guess = input() #user Guess a number

    
    if int(Guess)>secretNum:
        print('too high, Guess again')
    elif int(Guess)<secretNum:
        print('too low, Guess again')
    else:
        break
if int(Guess) != secretNum:
    print('No man, The num is : ' + str(secretNum))
else:
    print('You took ' + str(tries) + ' tries to guess the right number buddy')
