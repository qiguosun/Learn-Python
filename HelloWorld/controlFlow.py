age = 22
message = "Eligible" if age >= 19 else "bad"
print(message)
for number in range(1, 4):
    print("Attemp", number)
for number in range(1, 10, 2):
    print("Attemp", number)
# For .. Else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempt 3 times and failed")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
