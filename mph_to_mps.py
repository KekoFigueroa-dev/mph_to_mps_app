# Program: MPH to MPS Converter
# Description: This program converts miles per hour to meters per second

#====== Welcome Section ======#
# Display welcome message
print("Welcome to my MPH to MPS Conversion App")

#====== User Input Section ======#
# Get speed in MPH from user (allow decimals)
while True:
    try:
        speed_in_mph = float(input("What is your speed in MPH? "))
        break
    except ValueError:
        print("Please enter a valid number")

#====== Conversion Section ======#
# Convert MPH to MPS using conversion ratio (1 mph = 0.4474 mps)
speed_in_mps = speed_in_mph * 0.4474
# Round the result to 2 decimal places using round() function
speed_in_mps = round(speed_in_mps, 2)

#====== Output Section ======#
# Display the converted speed in MPS
print(f"Your speed in meters per second is {speed_in_mps}.")

print("Thank you for testing my app! ")
