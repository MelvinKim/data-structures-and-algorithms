# this is okay
import heapq
from collections import deque
import math
n = 0
print("n = ", n)

n = "abc"
print("n again = ", n)

# multiple assignments
n, m = 0, "abc"
n, m, z = 0, "abc", False

# incrementing a variabl
n = n + 1  # we can't do this: n++
n += 1

# Null value = none
# n = None

if n > 2:
    print("n is greater than 2")
elif n == 5:
    print("n is equal to five")
else:
    print("Default case")

# paranthesis are needed for multiline conditions
# and == &&
# or == ||
if ((n > 2 and
        n != m) or n == m):
    n + 1

# while loops
n = 0
while n < 5:
    print(n)
    n+1

# for loops
for i in range(5):
    print("i= ", 1)  # prints 0 - 4
# looping with start and end index (exclusive)
for i in range(2, 6):
    print("i=", i)  # prints 2 - 5
# reverse loop
for i in range(5, 0, -1):
    # prints 5 - 1, the end index is always exclusive
    print("i in reverse order = ", i)
for i in range(6, 3, -2):
    print("i in reverse order = ", i)  # prints from 6 - 2

# division is decimal division by default
print(5 / 2)  # prints 2.5
print(10 / 3)  # prints 3.333333

# to get integer division
print(5//2)  # prints 2
print(-3//2)  # prints -2
print(int(-3 / 2))  # prints -1

# modulus operator
print(10 % 3)  # prints 1
# NB, be careful when dealing with negative numbers
print(-10 % 3)  # prints -2
# To get a correct value, when dealing with negative numbers, do this instead
print(math.fmod(-10, 3))  # prints -1

# rounding down
print(math.floor(3/2))  # prints 1
# rounding up
print(math.ceil(3/2))  # prints 2
# finding squareroot
print(math.sqrt(3))  # prints 1.73205080
print(math.sqrt(4))  # prints 2.0
print(math.sqrt(9))  # prints 3.0
# power of a variable . eg 2 to power 3
print(math.pow(2, 3))  # prints 8.0

# geting Maximum integer (eg Integer.MAX in Java)
max = float("inf")
# geting Minimum integer (eg Integer.MIN in Java)
min = float("-inf")

# NB:
# - Python numbers are infinite, so they never overflow


# ARRAYS (list)
nums = [1, 2, 4]
# common operations
nums.append(5)  # add an element to the end of the array
nums.pop()  # removes from the end of the list , prints last element in the list
nums.insert(1, 7)  # takes O(N) Time
# reading and re-assigning values
nums[0] = 0  # O(1) Time
# initializing an array of a specific size
n = 5
arr = [1] * n
# reading last value of an array
lastElem = nums[-1]
# reading second last element
secondLastElem = nums[-2]
# getting sublists (slicing an array)
arr = nums[1:3]  # end index is exclusive
newArr = nums[0:4]
# unpacking an array
a, b, c = [1, 2, 3]
# looping througn an array
for i in range(len(nums)):
    print("element at index {} is {}".format(i, nums[i]))
for n in nums:
    print(n)
for i, n in enumerate(nums):  # getting access to the index and the value
    print(i, n)
# looping through multiple arrays simultaneously, with unpacking
# enables us to print the numbers in pairs eg [1,2] [3,4] [5,6]
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
# reverse an array
nums = [1, 2, 3]
nums.reverse()
# sorting an array
nums = [5, 4, 7, 3, 8]
nums.sort()  # in ascending order
nums.sort(reverse=True)  # in descending order
# sorting a list of strings based on alphabetical order
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
# implementing a custom sort eg based on the length
arr.sort(key=lambda x: len(x))
# list comprehension -> sort of an advanced way to initialize lists
arr = [i for i in range(5)]
arr = [i+1 for i in range(5)]
arr = [i*2 for i in range(5)]
# list comprehension for 2D lists
# prints [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr = [[0] * 4 for i in range(4)]
# prints [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
arr = [[1] * 2 for i in range(5)]


# STRINGS --> quite similar to arrays
s = "abc"
# slicing
str = s[0:2]
# strings are immutable --> You can't do this
s[0] = "A"
# updating a string --> creates a new string --> basically combining new strings to form a new one --> add to the end of the string
# modifying a string is an O(N) Time operation
s += "def"
# converting strings to integers to perform arithmetic operations
print(int("123") + int("123"))  # prints 246
# converting integers to strings
print(str(123) + str(123))
# getting the ASCII Value of a character
print(ord("a"))
print(ord("b"))
# combining a list of strings, (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))  # prints "abcdef"


# Queues (double ended queue)
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
# pop from the left of the queue in constant time
queue.popleft()  # O(1) time
# add values to the end of the queue
queue.appendleft(1)
# pop
queue.pop()


# Hashset
# we can search in O(1) Time, insert in O(1) Time
mySet = set()
mySet.add(1)
mySet.add(2)
# len of a set
n = len(mySet)
# check in element exists in the hashSet
containsOne = 1 in mySet
containsTwo = 2 in mySet
containsThree = 3 in mySet
# removing
mySet.remove(2)
# initialize a hashSet with a list of values
print(set([1, 2, 3, 5]))
# set comprehension in lists
mySet = {i for i in range(5)}  # {0,1,2,3,4}


# hashMap aka dictionary : Can't have duplicate keys
myMap = {}
myMap["alice"] = 88
myMap["melvin"] = 95
# length
n = len(myMap)
# modifying existing values
myMap["alice"] = 90
# seraching if contains a key
containsElement = "alice" in myMap
# removing a key from a map
myMap.pop("alice")
# initialize a hashMap
myMap = {"alice": 90, "bob": 70}
# dictionary comprehension
myMap = {i: 2*i for i in range(3)}  # prints {0: 0, 1: 2, 2: 4}
# looping through a map
myMap = {"alice": 90, "bob": 70}
# 1.
for key in myMap:
    print(key, myMap[key])
# 2.
for val in myMap.values():
    print(val)
# 3.
for key, val in myMap.items():
    print(key, val)


# Tuples are like arrays but IMMUTABLE
# - To initialize tuples, we use paranthesis rather than brackets eg tup = (1,2,3)
tup = (1, 2, 3)
num1 = tup[0]
num2 = tup[2]
# can't modify tuples
tup[0] = 0
# MAINLY used as keys for hashmaps or hashSets
# we do this, because lists aren't hashable and can't be keys eg myMap[[1,2]] = 5 --> cant't work
myMap = {(1, 2): 3}


# Heaps
# - used mainly for min and max problems
# - under the hood, they are basically arrays
# - by default, heaps in python are minHeaps
# - for minHeaps, the minimum value, will always be at index 0
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
# loop through
while len(minHeap):
    print(heapq.heappop(minHeap))
# - python, does not have max heaps by default
# - the workaround is to use min heaps and multiply by -1
# - when we push & pop
# - for maxHeaps, the maximum value will always be at index 0
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
# accessing the maximum value
maxValue = (-1 * maxHeap[0])
# looping
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
# building a heap from an intial set of values(list of values)
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))


# Functions
def addNum(x, y):
    return x + y

# nested functions
# - used alot expecially for recurssive problems


def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()


# Classes
class MyClass:
    # Constructor
    def __init__(self, nums):
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self keyword is required as a param, when creating a function inside a class
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


""" 
NB:
- Range always starts at 0 i.e
for i in range(5)
    print(i) --> prints 0,1,2,3,4
- heapify: build a heap from an initial set of values
arr = [2,1,8,4,5]
heapq.heapify(arr)
- self , is same as this keyword in other languages
"""