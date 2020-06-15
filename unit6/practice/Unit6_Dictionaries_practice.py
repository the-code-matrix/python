#!/usr/bin/python
# 1. Write a program to map given fruit name to its cost per pound.

#Solution:
item_cost={ 'banana': 0.69, 
            'apple' : 1.29,
            'pear' : 1.99,
            'grapes' : 2.49,
            'cherries' : 3.99 }
print("Cost of apple  per lb is: ",item_cost['apple'])
print("Cost of grapes per lb is: ",item_cost['grapes'])

# 2. Change cost of cherries to $4.99.

#Solution:
item_cost={ 'banana': 0.69, 
            'apple' : 1.29,
            'pear' : 1.99,
            'grapes' : 2.49,
            'cherries' : 3.99 }
item_cost['cherries'] = 4.99
print("Cost of cherries per lb is: ",item_cost['cherries'])

# 3. Write a python program to sum all the item's cost in a dictionary

#Solution:
item_cost={ 'banana': 0.69, 
            'apple' : 1.29,
            'pear' : 1.99,
            'grapes' : 2.49,
            'cherries' : 3.99 }
total_cost=0.0
for cost_of_each_item in item_cost.values() :
    total_cost += cost_of_each_item
print("Total cost: ", total_cost)

# 4. Display items of dictionary in sorted order by fruit name.

#Solution:
item_cost={ 'banana': 0.69, 
            'apple' : 1.29,
            'pear' : 1.99,
            'grapes' : 2.49,
            'cherries' : 3.99 }

for fruit in sorted(item_cost) :
    print(fruit, 'cost is ', item_cost[fruit])

#5. Write a program to map two lists into dictionary.

#Solution:
item_list = ['banana','apple','pear','grapes','cherries']
cost_list = [0.89, 2.19, 1.69, 2.79, 2.99]

# solution 1
item_cost = {}
for index in range(len(item_list)) :
    item_cost[item_list[index]] = cost_list[index]
print(item_cost)
# solution 2
item_cost = dict(zip(item_list, cost_list))
print(item_cost)
