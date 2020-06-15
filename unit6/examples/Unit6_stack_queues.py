#1. Write a program to implement stack using list.

#Solution
stack = []
for num in range(1, 16) :
    stack.append(num)

print (stack)

while len(stack) > 0 :
    print(stack.pop()),
print("")

#2. Write program to implement stack using list. The list elements are strings.

#Solution
stack = ["lego", "checkers", "monopoly",'connect','sequence'] 
print(stack)
print(stack.pop())
print(stack)
stack.append("scrabble") 
stack.append("chess")
print(stack) 
print(stack.pop())
print(stack) 

#3. Write a program to implement queue using list.

#Solution
queue = ["lego", "checkers", "monopoly",'connect','sequence'] 
print(queue)
queue.append("scrabble") 
queue.append("chess")
print(queue)
game = queue.pop(0)
print(game)
print(queue)

#4. Write a program to display size of queue.

#Solution
queue = [34,56,78,88,99]
print(queue)
print('Queue size',len(queue))
queue.append(99)
queue.append(102)
print (queue)
print('Queue size',len(queue))

#5. Write a program to pop each item in queue and check emptiness of queue using while loop.


#Solution
queue = ["lego", "checkers", "monopoly",'connect','sequence'] 
queue.append("scrabble") 
queue.append("chess")
print(queue)

while queue != [] :
    print(queue.pop(0)),
print("")