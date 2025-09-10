# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jimmy Ho
# Daniel Izmerly
# NAME Isaac Andrew Land
# Name: Nicholas Morales
# Section: ENGR-102-505
# Assignment: Team Lab 3 
# Date: 10 September 2025

import math
#
price_paid = float(input("How much did you pay? "))

price_cost = float(input("How much did it cost? "))

change = price_paid - price_cost

print(f"You received ${change:.2f} in change. That is...\n")

#Change Coins
quarter = 0.25

dime = 0.10

nickel = 0.05

penny = 0.01

num_quarters = change // quarter

change -= quarter * num_quarters


num_dimes = change // dime
change -= dime * num_dimes


num_nickels = change // nickel

change -= nickel * num_nickels

num_penny = int(round(change, 2) * 100) 
#daniels wonderful code, all written by him & Friends

if num_quarters == 0:
    pass
elif num_quarters == 1:
    print(f'{int(num_quarters)} quarter')
else:
    print(f'{int((num_quarters))} quarters')

if num_dimes == 0:
    pass
elif num_dimes == 1:
    print(f'{int(num_dimes)} dime')
else:
    print(f'{int((num_dimes))} dimes')


if num_nickels == 0:
    pass
elif num_nickels== 1:
    print(f'{int(num_nickels)} nickel')
else:
    print(f'{int((num_nickels))} nickels')

if num_penny == 0:
    pass
elif num_penny == 1:
    print(f'{int(num_penny)} penny')
else:   
    print(f'{int((num_penny))} pennies')

