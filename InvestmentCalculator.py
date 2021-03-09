# Capstone Project 1
# Writing a program for a small financial company to access financial calculators.

# Getting input from user on amount, rate, years and interest type to enter into investment calculator.
deposit_amount = int(input("Enter the amount in dollars that you are depositing:"))
interest_rate = float(input("Enter percentage of the interest rate:"))
num_years = float(input("Enter the number of years of the investment:"))
interest_type = input("Enter [Y] = simple or [N] = compound: ")

# Calculate simple interest and compound interest
simple = deposit_amount*interest_rate*(num_years/100)
compound = deposit_amount*((1 + interest_rate/100)**num_years)-deposit_amount

if interest_type == "Y":
    print("After [" + str(num_years) + "] years of investing at [" + str(interest_rate) + "%] interest rate, you will earn [$" + str(round(simple, 1)) + "].")
elif interest_type == "N":
    print("After [" + str(num_years) + "] years of investing at [" + str(interest_rate) + "%] interest rate, you will earn [$" + str(round(compound, 1)) + "].")
else:
    print("Please try again.")