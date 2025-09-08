# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Jimmy Ho
# Daniel Izmerly
# Isaac Andrew Land
# Nicholas Morales
# Section: ENGR-102-505
# Assignment: Team Lab 1 
# Date: 09/03/2025

import math

#user inputed number
user_number = float(input("Please enter the quantity to be converted: "))

#input|output
pounds_newtons = f'{(user_number * 4.44822):.2f}'  # With the help of Encando, adjusted conversion factor
meters_feet = f'{(user_number * 3.28084):.2f}'     # Adjusted conversion factor
atmo_kpasc = f'{(user_number * 101.325):.2f}'      # Adjusted conversion factor
watt_btu = f'{(user_number * 3.41214163):.2f}'     # This one is already correct
liter_gallon = f'{(user_number * 15.850323140625):.2f}'    # Adjusted conversion factor
celsius_fahrenheit = f'{(user_number * 9/5 + 32):.2f}'  # This one is already correct

user_number = f'{user_number:.2f}'

print(str(user_number), "pounds force is equivalent to", str(pounds_newtons), "newtons")
print(str(user_number), "meters is equivalent to", str(meters_feet), "feet")
print(str(user_number), "atmospheres is equivalent to", str(atmo_kpasc), "kilopascals")
print(str(user_number), "watts is equivalent to", str(watt_btu), "BTU per hour")
print(str(user_number), "liters per second is equivalent to", str(liter_gallon), "US gallons per minute")
print(str(user_number), "degrees Celsius is equivalent to", str(celsius_fahrenheit), "degrees Fahrenheit")
