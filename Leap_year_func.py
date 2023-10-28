# approach to determine if a given year is a leap year using a function in Python

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

#Input year
year = int(input("Enter the year : "))

# Check if it's a leap year using the function
if is_leap_year(year):
    print("Leap Year")
else:
    print("Not Leap Year")
