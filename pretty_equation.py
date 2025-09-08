# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
# Names:
# Jimmy Ho
# Daniel Izmerly
# Isaac Andrew Land
# Nicholas Morales
# Section: ENGR-102-505
# Assignment: Team Lab 3
# Date: 09/08/2025

# Pancake 24

import math

coefficient_A = int(float(input("Please enter the coefficient A: ")))
coefficient_B = int(float(input("Please enter the coefficient B: ")))
coefficient_C = int(float(input("Please enter the coefficient C: ")))

#Ax^2+Bx+C

equation = ("The quadratic equation is ")


#Coefficient A


#fabs checks for whether the coefficient is 1, 
#regardless of whether its positive or negative

if math.fabs(coefficient_A) == 1 or coefficient_A == 0:
    if coefficient_A == 1:
        equation += "x^2"
    elif coefficient_A == -1:
        equation += "- x^2"
    else:
        equation += ""
          
else:
    if coefficient_A > 0:
        equation += str(int(coefficient_A)) + "x^2"
    else:
        equation += "- %sx^2" % str(int(math.fabs(coefficient_A))) 



#coefficient B

if math.fabs(coefficient_B) == 1 or coefficient_B == 0:
    if coefficient_B == 1:
        equation += " + x"
    elif coefficient_B == -1:
        equation += " - x"


#If coefficient is positive, then add it, if coefficient is negative, then subtract it
else:
    if coefficient_B > 0:
        equation += " + %sx" % str(int(coefficient_B))
    else:
        equation += " - %sx" % str(int(math.fabs(coefficient_B))) 
          
#coefficient C


if coefficient_C == 0:
   equation += " "      
elif coefficient_C < 0:
    equation += " - " + str(int(math.fabs(coefficient_C)))
else:
    equation += " + " + str(int(coefficient_C))


print(equation, "= 0")




