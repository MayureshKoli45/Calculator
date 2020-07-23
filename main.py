print("WELCOME TO THE CALCULATOR")

# This loop is necessary to if you don't want your program to shut down.
while True:

    try:             # try and except block, used to continue the program even if the user puts a wrong input

        print("for ADDITION press 1 , for SUBTRACTION press 2 , for MULTIPLICATION press 3 , "
              "for DIVISION press 4 , to STOP press 5")  # Options for user to perform an operation

        opp = int(input())    # user input for operation

    # ADDITION
        if opp == 1:
            print("Enter first number:-")
            a = float(input())
            print("Enter second number:-")
            b = float(input())

            c = a+b
            print("Answer:-")
            print(c)

    # SUBTRACTION
        elif opp == 2:
            print("Enter first number")
            a = float(input())
            print("Enter second number")
            b = float(input())

            c = a-b
            print("Answer:-")
            print(c)

    # MULTIPLICATION
        elif opp == 3:
            print("Enter first number")
            a = float(input())
            print("Enter second number")
            b = float(input())

            c = a*b
            print("Answer:-")
            print(c)

    # DIVISION
        elif opp == 4:
            print("Enter first number")
            a = float(input())
            print("Enter second number")
            b = float(input())

            c = a/b
            print("Answer:-")
            print(c)

        elif opp == 5:         # to get out of this calculator
            break

        else:                  # if user puts a wrong input
            print("Wrong input")

    except Exception as e:
        print(e)
        print("invalid input")   # if user mistakenly input something else , this line will display

# this line displays when the user stops the calculator
print("Thank you for using this calculator\nhave a GOOD DAY")
