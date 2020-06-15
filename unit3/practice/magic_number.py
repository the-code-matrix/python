# Prompt the user to enter a number.
# Double the number. Add six. Divide in half.
# Subtract the original number.
# Print the result. (Hint: It'll always be the same number!)

number = int(input("Enter a number: "))
original = number # save original number for later

number *= 2
number += 6
number //= 2
number -= original

print(number)