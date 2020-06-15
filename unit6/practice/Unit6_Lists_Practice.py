#List Keywords
#Append 
#Insert
#Remove
#Pop 
#Clear
#Index
#Count
1. Given the following list, add the values 23 and 6 to the end of the list, and remove all values of 10 from the list. Print the answer.
nums = [2,4,4,5,4,7,9,10,11,4,15,16]


SOLUTION: 
nums.append(23)
nums.append(6)
nums.remove(10)
print(nums)


2. Using the final list you got as an answer to number 1, insert the value of 18 into index positions 5 and 8, and pop tha value at index 3. Print the answer.

SOLUTION:

nums.insert(5,18)
nums.insert(8,18)
print(nums)

3. Using the final list you got as an answer to number 2, print the index position of the value of 9 in the list. Finally, print the number of elements that have value 4.

SOLUTION: 

print(nums.index(9))
print(nums.count(4))

4. Erase all data from the entire list. Create a new list with any integer values you would like. Avoid syntax errors. Print your new list.

SOLUTION: 
nums.clear()
print(nums)
The students must create a new list while avoiding syntax errors.
EX list: 
nums = [2,4,4,5,4,7,9,10,11,4,15,16]
5. Loop through the list you have created. Print each number out as well as the index position of the integer. 


SOLUTION: 
Loop may look like this

for item in nums :
    print(item)
