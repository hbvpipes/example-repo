# PSEUDOCODE
# 1. Start the program.
# 2. Import the math module.
# 3. Present the menu to the user.
# 4. Print the menu options:
#    a. "Investment" - Calculate the amount of money that will be accumulated after a certain number of years.
#    b. "Bond" - Calculate the amount of money that you will need to pay back on a home loan.
# 5. Ask the user to choose an option from the menu.
# 6. Convert the user's choice to lowercase.
# 7. If the user chooses "investment", do the following:
#    a. Ask the user for the amount of money they want to deposit.
#    b. Ask the user for the interest rate (just a number, no % sign).
#    c. Ask the user for the number of years they want to invest for.
#    d. Ask the user for the interest type (simple or compound).
#    e. Convert the interest rate to a decimal.
#    f. If the interest type is "simple", calculate the total amount using : A = P * (1 + r*t),
#       where A is the total amount, P is the principal amount, r is the rate of interest, and t is the time in years.
#    g. If the interest type is "compound", calculate the total amount using A = P * math.pow((1 + r), t),
#       where A is the total amount, P is the principal amount, r is the rate of interest, and t is the time in years.
#    h. Print the total amount of money accumulated after the investment period.
# 8. If the user chooses "bond", do the following:
#    a. Ask the user for the present value of the house.
#    b. Ask the user for the interest rate.
#    c. Ask the user for the number of months to pay off the bond.
#    d. Convert the interest rate to a decimal and calculate monthly rate.
#    e. Calculate the monthly payment using: repayment = (i * P)/(1 - (1 + i)**(-n)).
#    f. Print the monthly payment.
# 9. If the user enters an invalid option, print an error message.
# 10. End the program.

import math  # Import the math module

# Menu Section
print("Welcome to the Investment and Bond Calculator")
print("Please choose one of the following options:")
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll need to pay back on a home loan")

# Get the user's choice and handle capitalization differences
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

# Investment Section 
if user_choice == 'investment':
    # Get the deposit amount from the user
    principal = float(input("Enter the amount of money you want to deposit: "))

    # Get the annual interest rate and convert it to decimal for necessary calculations
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100

    # Get the duration of investment in years
    years = int(input("Enter the number of years you want to invest for: "))

    # Ask whether the user wants simple or compound interest
    interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").strip().lower()

    # Calculate the simple interest
    if interest_type == 'simple':
        total_amount = principal * (1 + rate * years)
        print(f"The total amount after {years} years will be: R{total_amount:.2f}")

    # Calculate the compound interest
    elif interest_type == 'compound':
        total_amount = principal * math.pow((1 + rate), years)
        print(f"The total amount after {years} years will be: R{total_amount:.2f}")

    else:
        # Handle invalid interest type
        print("Invalid option. Please enter 'simple' or 'compound'.")

# Bond Section 
elif user_choice == 'bond':
    # Get the present value of the house (loan amount) and convert to float
    # Note: The user is expected to enter the present value directly
    present_value = float(input("Enter the present value of the house: "))

    # Get the annual interest rate and convert to decimal
    annual_rate = float(input("Enter the interest rate (as a percentage): ")) / 100

    # Get the number of months over which bond will be repaid and convert to integer
    # Note: The user is expected to enter the number of months directly
    months = int(input("Enter the number of months you want to pay off the bond: "))

    # Calculate the monthly interest rate by dividing the annual rate by 12
    monthly_rate = annual_rate / 12

    # Calculate the monthly repayment using the provided bond formula
    monthly_repayment = (monthly_rate * present_value) / (1 - math.pow((1 + monthly_rate), -months))

    # Show the result to the user and format it to 2 decimal places
    print(f"The monthly payment will be: R{monthly_repayment:.2f}")

# Error Handling for Invalid Menu Selection  
else:
    print("Invalid option. Please enter 'Investment' or 'Bond'.")

# End of Program