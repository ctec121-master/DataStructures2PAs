"""
CTEC 121
date: <ex: mm/dd/yyyy>
<your name>
"""

"""
INSTRUCTIONS:
READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE
0) The code below will not run. Your job is to fix it.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line or to 
   the right of the line that 1) describes the error and 2) describes what you
   did to fix the error.
3) Make sure the code runs.
4) Re-read steps 1 - 3.
"""


def main:
    print("This program calculates the future value of an investment.")
    print()

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input('Enter the number of years: ")

    print("Year   Value")
    print("------------")
    for i in range(years+1):
        print("{0:3}   ${1:7.2f".format(i, principal))
        principal == principal * (1 + apr)


main()
