# Function to find out if given year is a Leap Year or not.
def is_leap(target_year):
    if target_year % 4 == 0:
        if target_year % 100 == 0:
            if target_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function to return the month name and number of days in that month as a Dictionary.
def days_in_month(year, month):
    """Takes Year and Month number as input and returns
    the Month name and number of days in that month in a dictionary format."""
    month_days = [{"January": 31}, {"February": 28}, {"March": 31}, {"April": 30},
                  {"May": 31}, {"June": 30}, {"July": 31}, {"August": 30},
                  {"September": 30}, {"October": 31}, {"November": 30}, {"December": 31}]
    if month == 2 and is_leap(year):
        return {"February": 29}
    else:
        return month_days[month-1]


which_year = int(input("Enter the Year: \n"))
which_month = int(input("Enter the Month: \n"))
days = days_in_month(year=which_year, month=which_month)
for key in days:
    print(f"There are {days[key]} Days in the month of {key} of {which_year}!")