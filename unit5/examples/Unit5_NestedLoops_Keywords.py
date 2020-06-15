#Example1 - Using nested loops
import sys
for i in range(1,11):
   for j in range(1,11):
      k = i*j
      print (k, end=' ')


#KEYWORDS

#Example1 - Using Break
num = 0

for num in range(8):
    if num == 6:
        break    # break here

    print('Number is ', num)

print('Out of loop')

#Example2 - Using continue
for letter in "Python":     
   if letter == "t":
      continue
   print ("Current Letter :", letter)

#Example3 - Using pass
for letter in "Python": 
   if letter == "t":
      pass
      print ("The pass statement is used here")
   print ("Current Letter :", letter)