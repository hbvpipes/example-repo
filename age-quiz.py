# 1. Create an variable called age and assign it the value of the user's input.
# 2. The input should be converted to an integer.
# 3. Use the input to determine the user's age category and print a message accordingly.
# 4. The program should handle the following cases:
#    - If the age is greater than 100, print "Sorry, you're dead."
#    - If the age is 65 or older, print "Enjoy your retirement."   
#    - If the age is exactly 21, print "Congrats on your 21st!"
#    - If the age is 40 or older, print "You're over the hill."
#    - If the age is lower than 14, print "You qualify for the kiddie discount."
#    - For any other age, print "Age is just a number."
# 5. The program should be able to handle invalid inputs gracefully.


# Prompts the user for their age and print a message based on the age entered.
age = int(input("Please enter your age:"))

# Check if the age greater than 100
if age > 100: 
    print("Sorry, you're dead.") 

# Check the age entered is 65 or older
elif age >= 65:
    print("Enjoy your retirement.") 

# Check if the age entered is exactly 21
elif age == 21:
    print("Congrats on your 21st!")

# Check if the age entered is 40 or older
elif age >= 40:
    print("You're over the hill.")

# Check if the age is lower than 14
elif age < 13:
    print("You qualify for the kiddie discount.")

# Check if the age entered is any other number
else:
    print("Age is just a number.")