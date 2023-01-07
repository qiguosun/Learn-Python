# Handling Exceptions
# line 9 will always be excuted.
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("you didn't enter a valid age.")
#    print(ex)
#    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues.")


# Handling Different Exceptions

try:
    age = int(input("Age: "))
    xfactor = 10/age  # input 0 will return a zerodividing error
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were thrown")
