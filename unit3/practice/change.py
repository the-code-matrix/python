# Prompt the user for an amount of money in standard format (ex. 11.56).
# Print the number of dollars, quarters, dimes, nickels, and
# pennies that makes up the given amount of money.
# Hint: Convert the amount of money to cents.

# step 0: set constants (optional)
CENTS_PER_DOLLAR = 100  
CENTS_PER_QUARTER = 25  
CENTS_PER_DIME = 10  
CENTS_PER_NICKEL = 5  

# step 1: ask user to enter an amount of money
money = float(input("Enter an amount of money (omit the $): "))

# step 2: calculate the change

# convert to cents
remaining_amount = int(money * 100)

dollars = remaining_amount // CENTS_PER_DOLLAR  
remaining_amount %= CENTS_PER_DOLLAR  

quarters = remaining_amount // CENTS_PER_QUARTER  
remaining_amount %= CENTS_PER_QUARTER  

dimes = remaining_amount // CENTS_PER_DIME  
remaining_amount %= CENTS_PER_DIME  

nickels = remaining_amount // CENTS_PER_NICKEL  
remaining_amount %= CENTS_PER_NICKEL  

pennies = remaining_amount  

# step 3: print the results
print("Your amount $" + str(money) + " consists of")  
print("\t" + str(dollars) + " dollars")   # tab character \t, newline character \n
print("\t" + str(quarters) + " quarters")  
print("\t" + str(dimes) + " dimes") 
print("\t" + str(nickels) + " nickels")  
print("\t" + str(pennies) + " pennies")  