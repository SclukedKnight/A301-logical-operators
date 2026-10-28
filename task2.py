#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and divisible by 2.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a divisible by 2.
xx is only a perfect square.
xx is only divisible by 2.

Example:
Enter a number: 8
8 is only divisible by 2.

Enter a number: 64
64 is both a perfect square and divisible by 2.
"""
num = float(input("Enter number to be checked: "))

if not num < 0:
    if round(num ** (1/2)) == int(num ** (1/2)) and num % 2 == 0:
        print("This number is a perfect square and divisable by 2")
    elif round(num ** (1/2)) == int(num ** (1/2)) and not num % 2 == 0:
        print("This numver is a perfect square and NOT divisable by 2")
    elif not round(num ** (1/2)) == int(num ** (1/2)) and num % 2 == 0:
        print("This isn't a perfect square but is divisable by 2")
    else:
        print("This number ins't a perfecr square or divisable by 2")