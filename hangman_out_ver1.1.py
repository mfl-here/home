import random
word_list = ["fahad"]
word = random.choice(word_list)
life = 10
unknown_list = list("_"*len(word))
unknown = ""
while unknown!=word:
    guess = input("Enter the letter: ")
    if len(guess) == 1:
        if guess in word:
            for j in range(0,len(word)):
                if guess == word[j]:
                    unknown_list.insert(j,guess)
                    unknown_list.pop(j+1)
            print(unknown_list)
            if unknown_list == list(word):
                print("Congrates! You win")
                break
            else:
                pass
                
        else:
            life -=1
            if life == 9:
                print('''
    
        |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            if life == 8:
                print('''
    -------
        |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            elif life == 7:
                 print('''
    -------
        |   |
            |
            |
           
                ''')
                 print("Wrong guess!")
                 print("You have",life,"Left")
                 continue
            elif life == 6:
                 print('''
    -------
        |   |
            |
            |
           ---
                ''')
                 print("Wrong guess!")
                 print("You have",life,"Left")
                 continue
            elif life == 5:
                print('''
    ---------
        |     |
       O    |
              |
              |
           ---
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            elif life == 4:
                print('''
    ----------
        |      |
       O     |    
        |      |
               |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            elif life == 3:
                print('''
    ----------
        |      |
       O     |    
     /  |      |
               |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            elif life == 2:
                print('''
    ----------
        |      |
       O     |    
     /  |  \   |
               |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            elif life == 1:
                print('''
    ----------
        |      |
       O     |    
     /  |  \   |
       /       |
                ''')
                print("Wrong guess!")
                print("You have",life,"Left")
                continue
            else:
                print('''
    ----------
        |      |
       O     |    
     /  |  \   |
       / \     |
                ''')
            print("Wrong guess!")
            print("Oops you died")
            break
    else:
        print("Only one letter at a time")
else:
    for i in unknown_list:
        unknown = unknown + i
                    
print(unknown)           
