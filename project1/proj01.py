################################################################
#  Computer Project #1 
#   Algorithm
#   prompt for a floating-pint value represnting a distance \
#   in rods
#   display results of calculations
#   convert to meters, feet, miles, furlongs and the time \
#   in minutes to walk that distance
#   display results of calculations
################################################################

#conversion for each unit
METERS_PER_ROD=5.0292
RODS_PER_FURLONGS=40
METERS_PER_MILES=1609.34
METERS_PER_FEET=0.3048
SPEED_MILES_PER_HOUR=3.1

#prompt for a floating-pint value represnting a distance in rods
rods_str = input("Input rods: ")
rods_float=float(rods_str)
print("You input",rods_float,"rods.")

#display a blank line
print()

# convert rods to meters
print("Conversions")
print("Meters:", round(float(rods_str)*METERS_PER_ROD,3))

#convert meters to feet
meters_float=float(rods_str)*METERS_PER_ROD
print("Feet:", round(meters_float/METERS_PER_FEET,3))

#convert meters to mile
miles_float=float(meters_float/METERS_PER_MILES)
print("Miles:", round(miles_float,3))

#convert rods to furlong
print("Furlongs:", round(rods_float/RODS_PER_FURLONGS,3))

#convert hours to walk to minutes to walk, 1hour=60 minutes
speed_miles_per_minutes=SPEED_MILES_PER_HOUR/60
speed_float= float(speed_miles_per_minutes) 
print("Minutes to walk", rods_float,"rods:",round(miles_float/speed_float,3))


