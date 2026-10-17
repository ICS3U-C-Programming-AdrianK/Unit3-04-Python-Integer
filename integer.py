#!/usr/bin/env python3
# created by : Adrian student
# date : 17th OCT 2026
# This program asks the user for an integer and then
# tells the user if the integer entered is positive ,
# negative or equal to 0
def main():
    # get the user integer
    user_integer = int(input("Enter your integer : "))

    # Determine the nature of the integer
    if user_integer > 0:
        print("{} is a positive number".format(user_integer))
    elif user_integer < 0:
        print("{} is a negative number".format(user_integer))
    elif user_integer == 0:
        print("{} is just zero".format(user_integer))
    else:
        print("No idea")


if __name__ == "__main__":
    main()
