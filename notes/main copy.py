n = 0

# single line multiple assignment
n, m = 0, "abc"
print('n = ', n)
n, m, z = 0.125, "abc", False
print('z = ', z)

# Increment
n = n + 1
n += 1
# n++ --> can't do this

# None is null (absence of value)
n = 4
x = None

# if statement / conditionals do not need paranthesis -> use identation
if n > 2:
    n = n - 1
elif n < 2:
    n = n * 2
else:
    print(n)
    
# logic conditionals
# && --> and
# || --> or

# Paranthesis are needed for multiline conditions
n, m = 1, 2
if ((n > 2 and
    n != m) or n == m):
    n = n + 1

# for loops in python : from i = 0 to i = 4
for i in range(5):
    print(i)  
for i in range(2, 6): #from i = 2 to i = 5 , last number is exclusive
    print("inner for loop value: ", i)

# reverse for loop
for i in range(5, 1, -1): #starts from i = 5 to i = 2
    print("reverse for loop: ", i)
  
# while loops in python
n = 0
while n < 5:
    # print(n)
    n = n + 1
    
# Division is decimal division by default
print( 5 / 2) # prints 2.5

# if you want integer division , use double slash
print(5 // 2) # prints 2

# modulus operator
print(10 % 3)

# maximum integer
max = float("inf")

# minimum integer
min = float("-inf")


# Arrays in python --> called lists in python --> they are dynamic
nums = [1,2,3,4,5,6]
nums.append(7) # pushes to the end
nums.append(8)
nums.pop() # pops from the end
nums.insert(0, 0) # O(n) operation
nums[0] = 0 # O(1) operation
nums[1] = 9 # O(1) operation
print("nums array: ", nums)

# Initialise an array of size n with default values
n = 5
arr = [1] * n

# accessng the last element in an array
print(arr[-1])

# accessing the second last element
print(arr[-2])

# get sublists , or slicing an array
print(arr[1:3]) # last index is exclusive
print(arr[0:4])

# unpacking
a, b, c = [1, 2, 3]  
# NB: number of elements on the right, has to be equal to the number of elemnets on the left : a, b = [1,2,4] --> can not do this

# looping over an array