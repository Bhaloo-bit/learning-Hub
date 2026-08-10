#1. rolling a pair of dice
import random
request = input("Roll the dice ?, (y/n) :")


if (request == "y" or request == "Y"):
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    print(result1 , result2)
elif(request == "n"or request == "N"):
    print("Thanks for playing ")    
else :
    print("! Invalid entry")    

#2. Guessing the Number 

import random
gen_number = random.randint(1, 100)
print(gen_number)

while True:
    try:
        guess_no = int(input("Enter a Number between 1 to 100: "))
        
        if guess_no > gen_number :
            print("! Too High")
        elif guess_no < gen_number :
            print("! Too low")
        else:
            print("Congratulation! You Found the Number5")
            break
    except ValueError:
        print("Enter a valid number")  





    


