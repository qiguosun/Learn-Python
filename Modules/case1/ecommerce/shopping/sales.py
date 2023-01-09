# a relative import


def calc_tax():
    pass


def calc_shipping():
    pass

#  with the following code, we can make the file usable as a script,
#  as well as a reusable module that we can import into another module.

if __name__ == "__main__":
    print("Sales started")
    calc_tax()
    