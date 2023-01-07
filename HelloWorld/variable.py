import math
first = "qiguo"
last = "sun"
course = "  Python programming"
print(f"{first} {last}")
print(first.upper())
print(first.title())
print(course.strip())
print(course.find("pro"))
print("pro" in course)

# number
x = 1
x = 1.1
x = 1 + 2j
print(x+3j)
print(10/3)
print(10//3)
print(10 % 3)

# working with number

print(round(2.9))
print(math.ceil(2.2))  # get 3

# type conversion
x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
