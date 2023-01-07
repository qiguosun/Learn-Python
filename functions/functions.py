# xargs example
def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)

# xxargs example
# pass key~value pairs, python automatically package them into a dictionary


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="John", age=22)
