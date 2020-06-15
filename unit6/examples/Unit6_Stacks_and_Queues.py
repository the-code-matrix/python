from collections import deque
#Example1
stack = [3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)
print(stack)

#Example2

stack.pop()
print(stack)
stack.pop()
print(stack)

#Example3

queue = deque(["Python", "C++", "Java"])
print(queue)
queue.append("C")           
queue.append("C#")
print(queue)

#Example4
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")          
queue.append("Graham")


print(queue)          
queue.popleft()
print(queue)                 
queue.popleft()                 
print(queue)
