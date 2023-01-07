# Stacks
# use list append() list pop()

# queue
from sys import getsizeof
from array import array
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


# tuples
# A read only list
point = (1, 2)


# swap variables
x = 10
y = 11
x, y = y, x
print("x:", x, "y", y)


# Array
# unlike an list, every object is typed.
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(3, 2)
numbers.pop()


# Set
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
second = {1, 5}
# second.add(5)
# second.remove(1)
first = {2, 3, 1}
# get union of the two set
print("-"*10)
print(first | second)
print(first ^ second)
print(first & second)
print(first - second)


# Dictionaries
point = {"x": 1, "y": 2}
# a better method
point = dict(x=1, y=2)
print(point)
print(point["x"])
point["z"] = 30
if "a" in point:
    print(point["a"])
print(point.get("a"))
print(point.get("a", 0))  # if key a does not exist, return 0
del point["x"]
for key in point:
    print(key, point[key])
for x in point.items():
    print(x)
# unpack the turple
for key, value in point.items():
    print(key, value)


# Dictionary Comprehensions
values = []
for x in range(5):
    values.append(x*2)
# [expression for item in items]
values = [x*2 for x in range(5)]
values = {x*2 for x in range(5)}
values = {x: x*2 for x in range(5)}
print(values)

# Generator expressions
# if the data is large, it is inefficient to store them in the memory
# For example list: [x * 2 for x in range(10)] can be write as follows as a generator
values = (x*2 for x in range(10))
print(values)
for x in values:
    print(x)
# get the size of a iterator
print("gen:", getsizeof(values))
values = [x*2 for x in range(10)]
print("list:", getsizeof(values))
values = (x*2 for x in range(100))
print("gen:", getsizeof(values))
values = [x*2 for x in range(100)]
print("list:", getsizeof(values))


# unpacking Operator
numbers = [1, 2, 3]
print(*numbers)
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
