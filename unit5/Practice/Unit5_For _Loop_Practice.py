1. Loop through the string "Programming" and print each letter on each line.

Solution: 
 
for letter in "Programming":
    print("The current letter is", letter)


2. Loop through the following list and print each element.
List: ["Basketball", "Baseball", "Football", "Hockey", "Soccer"]


SOLUTION: 
List: ["Basketball", "Baseball", "Football", "Hockey", "Soccer"]
for item in lst:
    print(item)



3. Find the sum of the first 300 natural numbers (1,2,3,....,300) using the RANGE function. Note any differences from using a while loop and a for loop.



Solution: 

sum = 0
for num in range(1, 301):
    sum = sum + num
    print("The total sum is:", sum)



4. Iterate list using index and range with for loop.
genre = ['pop', 'rock', 'jazz']


Solution:
for index in range(len(genre)) :
    print("I like ", genre[index])

5. Find greatest number in give list of numbers using for loop.
num_list=[23,45,67,2,3,5,78,89,3]


Solution:
max_num = 0
for index in range(len(num_list)) :
    if num_list[index] > max_num :
        max_num = num_list[index]
print("Greatest number is ", max_num)