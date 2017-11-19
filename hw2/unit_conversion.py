###############################################
#####  Vincent O'Leary (vjo25)            #####
#####  Assignment 2 for CS 171-064        #####
#####  Unit Conversion Calculator         #####
###############################################

#Print welcome statement and valid inputs
print(
    "Welcome to the length conversion wizard.\n"
    "This program can convert between any of the following lengths.\n"
    "inches\n"
    "feet\n"
    "yards\n"
    "miles\n"
    "leagues\n"
    "centimeters\n"
    "decimeters\n"
    "meters\n"
    "decamters\n"
    "hectometers\n"
    "kilometers\n"
    "Note: You must use the units exactly as spelled above.\n"    
    )
    
#Create dictionary based on 1 meter base unit
dict={
    "inches":0.0254,
    "feet":0.3048,
    "yards":0.9144,
    "miles":1609.3440000000103,
    "leagues":4828.041699999944,
    "centimeters":0.0100,
    "decimeters":0.1000,
    "meters":1.0000,
    "decameters":10.0000,
    "hectometers":100.0000,
    "kilometers":1000.0000 
}

#Ask for inputs
print("Enter value:")
value_input=float(input())
print("Enter current units:")
unit_input=input()
print("Enter target units:")
unit_output=input()

#Convert from input units to base units
value_base=value_input*dict[unit_input]

#Convert from base units to output units
value_output=value_base/dict[unit_output]

#Print conversion
print("{0:.4f}".format(value_input),unit_input,"is equal to","{0:.4f}".format(value_output),unit_output)