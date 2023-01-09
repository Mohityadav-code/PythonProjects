# rating 1 to 5
# App => rating (1,5)
# if rate<1 or rate>5:
#     error
#     try again
# else:
#     thank you


flag = 1


while flag == 1:
    a = int(input("Enter your rating between 1 to 5 : "))
    if (a < 1) or (a > 5):
        print("try again")
    else:
        print("Thank you")
        flag = 0
