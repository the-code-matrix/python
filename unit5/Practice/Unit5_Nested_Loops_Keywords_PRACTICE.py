Display multiplication table of 2 to 6.

Solution:
for table in range(2,7) :
    factor=12
    while factor > 0 :
        print(table,"x",factor, "=", table*factor)

2. Display possible combination lunch using one item from each of the following lists.
main_list=["sandwitch", "burrito", "burger"]
side_list=["french fries","onion rings","mozzarella sticks"]


Solution:
for main_item in main_list :
    for side_item in side_list :
        print(main_item, side_item)

3. Display prime numbers from 2 to 50.


Solution:
i = 2
while(i < 50):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

4.  Display traingle shape using *.

Solution:
for i in range(1,7):
    for j in range(i):
        print("*"),
    print("")

5. Display Square shaping using character 'x' and each side of has 5 x's


Solution:
for i in range(6) :
    for j in range(6):
        print("x"),
    print("")
    