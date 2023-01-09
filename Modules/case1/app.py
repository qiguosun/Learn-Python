from ecommerce.shopping.sales import calc_shipping, calc_tax
import ecommerce.shopping.sales as sales
from ecommerce.shopping import sales
import sys

print(sys.path)
print(dir(sales))
calc_shipping()
calc_tax()
sales.calc_shipping()


# when add __init__.py to ecommerce, python will treat the ecommerce forlder as a package
# A package is a container for one or more modules.
# A package is mapped to a directory and a module is mapped to a file.
