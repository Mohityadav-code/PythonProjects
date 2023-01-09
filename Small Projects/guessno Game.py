import random
#guessing game

print("Welcome to guessing game")

#creating variable
a=int(input("Enter a Random no. between 1 to 10 "))
guess_num = random.randint(1, 10)




for i in range(0,10):
    if a==guess_num:
        print("Hey you got it Amazing !!")
        print("so the random no. is", guess_num)
        break
    else :
        print("Sorry try again")  
    a=int(input("Enter a Random no. between 1 to 10 "))
    


print(guess_num)


