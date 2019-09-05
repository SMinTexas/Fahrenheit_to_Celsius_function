# Write a function that takes a temperature in Fahrenheit, converts it to Celsius,
# and returns the value.
#
# The formula to convert a temperature from Fahrenheit to Celsius is:
# C = (F - 32) * 5/9

def f_to_c(F):
    return (F - 32) * 5/9

# Main program flow
Fahrenheit = float(input("Please enter today's temperature in Fahrenheit "))
print(f"Today's temperature in Celsius will be {f_to_c(Fahrenheit)} degrees.")