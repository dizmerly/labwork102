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

#Linear interpolation for x, y, and z axis
def linear_interpolation(t0, t1, p0, p1, t):
    return (((p1 - p0)/(t1 - t0)) * (t - t0)) + p0


#Initial set time and coordinates
t0 = float(input("Enter time 1: "))
x0 = float(input("\nEnter the x position of the object at time 1: "))
y0 = float(input("\nEnter the y position of the object at time 1: "))
z0 = float(input("\nEnter the z position of the object at time 1: "))

#Final set time and coordinates
t1 = float(input("\nEnter time 2: "))
x1 = float(input("\nEnter the x position of the object at time 2: "))
y1 = float(input("\nEnter the y position of the object at time 2: "))
z1 = float(input("\nEnter the z position of the object at time 2: "))
#The time at which we want to find the object's position
# t = int(input("Time in minutes: "))
t = t0

#The starting and ending times for linear interpolation
a0 = t0
a1 = t1

#Calculating evenly spaces between the start and end times for linear interpolation
distance_between = a1 - a0
partitions = 4
#The number is 4 instead of 5 because thinking it like a piece of chocolate, you need four slices to get five pieces, and because the initial number counts towards an interpolation point
s = distance_between / partitions

#First Interpolation
Final_X_Pos = linear_interpolation(t0, t1, x0, x1, t)
Final_Y_Pos = linear_interpolation(t0, t1, y0, y1, t)
Final_Z_Pos = linear_interpolation(t0, t1, z0, z1, t)
print(f"\nAt time {t:.2f} seconds the object is at ({Final_X_Pos:.3f}, {Final_Y_Pos:.3f}, {Final_Z_Pos:.3f})")

#Second Interpolation
t = t + s
Final_X_Pos = linear_interpolation(t0, t1, x0, x1, t)
Final_Y_Pos = linear_interpolation(t0, t1, y0, y1, t)
Final_Z_Pos = linear_interpolation(t0, t1, z0, z1, t)
print(f"\nAt time {t:.2f} seconds the object is at ({Final_X_Pos:.3f}, {Final_Y_Pos:.3f}, {Final_Z_Pos:.3f})")

#Third Interpolation
t = t + s
Final_X_Pos = linear_interpolation(t0, t1, x0, x1, t)
Final_Y_Pos = linear_interpolation(t0, t1, y0, y1, t)
Final_Z_Pos = linear_interpolation(t0, t1, z0, z1, t)
print(f"\nAt time {t:.2f} seconds the object is at ({Final_X_Pos:.3f}, {Final_Y_Pos:.3f}, {Final_Z_Pos:.3f})")

#Fourth Interpolation
t = t + s
Final_X_Pos = linear_interpolation(t0, t1, x0, x1, t)
Final_Y_Pos = linear_interpolation(t0, t1, y0, y1, t)
Final_Z_Pos = linear_interpolation(t0, t1, z0, z1, t)
print(f"\nAt time {t:.2f} seconds the object is at ({Final_X_Pos:.3f}, {Final_Y_Pos:.3f}, {Final_Z_Pos:.3f})")

#Fifth Interpolation
t = t + s
Final_X_Pos = linear_interpolation(t0, t1, x0, x1, t)
Final_Y_Pos = linear_interpolation(t0, t1, y0, y1, t)
Final_Z_Pos = linear_interpolation(t0, t1, z0, z1, t)
print(f"\nAt time {t:.2f} seconds the object is at ({Final_X_Pos:.3f}, {Final_Y_Pos:.3f}, {Final_Z_Pos:.3f})")