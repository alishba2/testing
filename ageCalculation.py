#age calculation
#import dateTime to get current date, year, month, etc.
import datetime

#function to calculat the age in year
def ageCalculation(year):
    # using dateTime library to get the current year
    presentDate= datetime.datetime.now()
    presentYear = presentDate.year
    calculatAge = presentYear - year 
    return calculatAge

# Get user input ( year )
print("Enter your Birth year")
year = int(input())

#function call to calculat the age in years
age = ageCalculation(year)
print(" your Age is (year) :" , age)
