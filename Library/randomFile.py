import random
import string


print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 3, 4, 5, 2]))
print(random.choices([1, 3, 4, 5, 2], k=2))
print("".join(random.choices(string.ascii_letters+string.digits, k=6)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
