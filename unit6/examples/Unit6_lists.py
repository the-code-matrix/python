#List Keywords
#Append 
#Insert
#Remove
#Pop 
#Clear
#Index
#Count

nums = [3,4,5,7,9,10]

# display all elements
print (nums)

#append (add at the end) number to list:
nums.append(6)
print (nums)

#insert element at index 2
nums.insert(2,88)
print(nums)

#remove element with value 9
nums.remove(9)
print(nums)

#pop element at 4th index
nums.pop(4)
print(nums)

#clear list, removes all data
nums.clear()
print(nums)

nums = [3,4,5,7,9,10,9]
print (nums)
#index of element with value 10
print(nums.index(10))

#list - number of elements
print(nums.count(9))

# loop  through list entries
print("Loop through list:")
for item in nums :
    print(item)


