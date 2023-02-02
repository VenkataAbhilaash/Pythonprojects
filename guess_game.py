# Guessing Game

from random import randint

number1=randint(1,100)

plnumber=int(input("Enter a number:"))
previous_number=0
turns=1
while plnumber!=number1:
    if plnumber<1 or plnumber>100:
        previous_number=plnumber
        plnumber=int(input("Choose a number between 1 and 100"))
        turns+=1
    elif abs(plnumber-number1)<=10:
        print("WARMER")
        turns+=1
    elif abs(plnumber-number1)<=5:
        print("You are almost there.")
        turns+=1
    elif abs(plnumber-number1)>20:
        print("Decrease your ditance by 20 up or down.")
        turns+=1
    else:
        print('COLDER')
        turns+=1
    plnumber=int(input("Choose a number between 1 and 100"))
else:
    print(f"You have guessed the number in {turns} turns")