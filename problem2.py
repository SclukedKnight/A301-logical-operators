#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

list = [num1, num2]
list.sort()

if list[1] / list[0] == int(list[1] / list[0]):
    print(f"{list[0]} is factorable from {list[1]}")
else:
    print(f"{list[0]} isn't factorable from {list[1]}")