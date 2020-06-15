1. Write a while loop printing the first 15 natural numbers (1,2,3,4....)


SOLUTION: 
count = 1
while count < 15:
    print(count)
    count = count + 1

2. Write an infinite while loop.


SOLUTION:
x = 0
while x < 1:
    print("This loop runs forever")



3. Write a while loop that prints the 12th multiplication table uptil 12 * 10.



SOLUTION: 
x = 1

while x < 11:
    product = 12 * x
    print("12 * ", x, "is", product)
    x = x + 1

4. Write a while loop that prints all numbers from 100 to 1.


SOLUTION:
count = 100
while count > 0:
    print(count)
    count = count - 1


5. Write a while loop that prints the sum of all numbers from 1 to 200.

count = 1
sum = 0

while count < 201:
    sum = sum + count
    print(sum)
    count = count + 1
