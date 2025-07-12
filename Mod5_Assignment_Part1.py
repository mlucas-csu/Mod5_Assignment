# Part 1

# User inputs number of years
num_years = int(input("How many years do you want to collect the average rainfall for? "))

# Creating a list to iterate through for each month in the year
year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Initializing the variable i for the number of years in the while loop
i = 1
# Initializing the total_rain variable with zero before both loops
total_rain = 0

# Creating the while loop that starts at 1 and ends when i reaches the number of years input by the user
while i <= num_years:
    # Creating the for loop that will run 12 times for each year input by the user
    for month in year:
        # User inputs total rainfall for each month in the iteration
        monthly_rainfall = int(input("How many inches of rainfall was there in {} of year {}? ".format(month, i)))
        # total_rain variable is incremented by the amount of rainfall for each month
        total_rain = total_rain + monthly_rainfall
    # Once 12 months are completed in the for loop, the next year begins (if applicable) for the while loop
    i += 1

# Simple calculation to output the total number of months measured
sum_months = num_years * 12
print("Number of months: ", sum_months)

# Outputting total inches of rainfall for entire period
print("Total inches of rainfall: ", total_rain)

# Average rainfall per month for entire period
average_rainfall_month = total_rain / sum_months
print("Average rainfall per month for entire period: {:.2f} inches".format(average_rainfall_month))

