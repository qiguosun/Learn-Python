# problem： if line 5 or 6 enconter exception, the file cannot be cloased
# With statement is used to automatically release external resources.
# if a class have __enter__ and __exit__, we can use the object with "with" statement

try:
    # file = open("cleaningUp.py")
    with open("Exceptions/theWithStatement.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10/age  # input 0 will return a zerodividing error
    # file.close()
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were thrown")
