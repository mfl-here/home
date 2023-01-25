import random
main = ["webcam","python","windows","graphicscard","instagram","keyboard","motherboard","time machine"]
on = random.choice(main)
life = 6
start =0
msg = ""
guess = ""
pts = 0
print(
'''HOW TO PLAY:
*Guess the correct letters of the word inorder to win.
*You have 6 lives to play. Every wrong guess will cost 1 life.
*All Words is related to computer.
POINTING:
*For every correct guess 2 pts will be awarded
''')
i = 0
while life != 0 or guess!=on:
    for i in range(start,len(on)):
        msg = "Enter"+str(i+1)+"letter: "
        letter = input(msg)
        if letter.lower() == on[i]:
            start+=1
            pts +=2
            guess = guess + letter.lower()
            print("correct guess")
            break
        else:
            life -=1
            print("wrong guess! You have",life,"lives left")
            break
            
        
if guess == on:
    print("Congrats you win!")
    print("You win",pts,"points")
else:
    print("Oops! You die :( The word was",on,"\nBetter luck next time")
    print("You win",pts,"points")
    
