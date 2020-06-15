

These exercises will simulate a real programming experience. You will create your own data and data structures and you will use the methods that are built in or import some methods.


1. Create a list with any variable name. Use the append(), insert(), remove(), and pop() methods to alter your list in any way. Ensure that if you run into syntax errors, try your best to solve them!

SOLUTION:

Ensure that there are no syntax errors. Methods should be implemented in the same manner shown below

nums.append(6)
print (nums)


nums.insert(2,88)
print(nums)

nums.remove(9)
print(nums)

nums.pop(4)
print(nums)


2. Create a loop to loop and print out your list. This time, add comments in your program saying what you think is going in each step of the program


SOLUTION: 


for item in nums : #iterates through the list named nums
    print(item)   #prints out each item in the list
                  #ends when there are no more elements in the list


3. Create your own tuple and have it contain at least 8 elements . In the tuple, access the 2nd and 5th index positions.

t =  'start', 76 , 'hello!', 4242, 'bye', '34', '2323', 'end'
print(t[2])
print(t[5])


4. Create a dictionary. Add two new unique keys with a value. Print the new dictionary. Next, use the delete() method to delete any key and its value. Finally, loop through the dictionary using a for loop.


SOLUTION:

print(languages)
languages = {'Python': 4098, 'Java': 4139, 'C++': 9234}
languages['C'] = 3224
print(languages)

print(languages)
del languages['C++']
print(languages)

for k, v in languages.items():
    print(k,v)


5. Create a stack and queue. For the queue ensure to use the (from collections import deque) statement at the top of your program. 
   Remember, to use queues , you have to use the following format queue = deque(["Eric", "John", "Michael"]) and use the popleft() and append() methods

For the stack, add two elements to the end of the stack and then pop one back out. Print the final stack

For the queue, add three elements to the end of the queue and then use popleft() to remove one element from the front of the queue. Print the final queue.


SOLUTION: 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
print(stack)

queue = deque(["Python", "C++", "Java"])
queue.append("C")           
queue.append("C#")
queue.append("Javascript")
print(queue)          
queue.popleft()
