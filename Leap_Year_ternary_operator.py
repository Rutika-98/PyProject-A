# approach using a ternary conditional operator to determine if a given year is a leap year in Python

year = int(input("Enter the year : "))

# Use a ternary conditional operator to check if it's a leap year
leap_year = "Leap Year1"if(year % 4 == 0 and year %100 !=0) or (year % 400 ==0) else "Not Leap Year"

print(leap_year)