print("we are going to make simple calculator")
while(1):
    print("Enter 0 for the exit from calcualtor")
    print("Enter Respected Number for calcualtion")
    print("1. for addition\n 2.for Substactio\n 3. for multiplication \n 4' for division")
    user_number_caculation=int(input("enter number"))
    if user_number_caculation==0:
        exit()
    else:
        user_choice1=int(input("enter first number"))
        user_choic2=int(input("enter seconda NUmber"))
        match user_number_caculation:
            case 1:
                sum=user_choice1+user_choic2
                print("sum is ",sum)
            case 2:
                subtraction=user_choice1-user_choic2
                print("subtraction is",subtraction)
            case 3:
                multiplication=user_choic2*user_choice1
                print("Multiplication is",multiplication)
            case 4:
                try:
                    print(user_choice1/user_choic2)
                except ZeroDivisionError as e:
                    print("your dinominator can not be zero")
            case _:
                print("BYe Bye tata see you")
                exit()
                 