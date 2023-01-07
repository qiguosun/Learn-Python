letters = ["A", "B"]
zeros = [0] * 5
combined = zeros + letters
print(combined)

numbers = list(range(20))
print(numbers)


chars = list("Hello World")
print(chars)

letters = ["a", "b", "c", "d"]
print(letters[::2])  # b and d will be skipped
print(letters[::-1])  # reverse a list


# list unpacking
numbers = [1, 2, 3, 4, 5, 6]
first, *other, last = numbers
print(first, last)
print(other)


# Add
letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
print(letters)
letters.remove("b")  # remove the first
del letters[0:3]
print(letters)


# Finding items
letters = ["a", "b", "c", "d"]
print(letters.index("a"))


# Sorting lists
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(sorted(numbers, reverse=True))
print(numbers)
# sort tuple need to give a key~function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# Lambda function: an oneline anonymous function that can pass to other function
# items.sort(key=lambda parameter:expression)
items.sort(key=lambda item: item[1])
print(items)


# Map Function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
x = map(lambda item: item[1], items)
for item in x:
    print(item)
print(list(map(lambda item: item[1], items)))


# Filter Function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
x = filter(lambda item: item[1] > 10, items)
print(list(x))


# List Comprehensions
# [expression for item in items]
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]


# Zip funtion
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(zip(list1, list2))
print(list(zip(list1, list2)))  # [(1,10),(2,20)...]
