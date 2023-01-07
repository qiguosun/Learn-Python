# problem： if line 5 or 6 enconter exception, the file cannot be cloased

try:
    file = open("cleaningUp.py")
    age = int(input("Age: "))
    xfactor = 10/age  # input 0 will return a zerodividing error
    # file.close()
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()
