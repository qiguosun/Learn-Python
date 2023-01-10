import csv

with open(r"Library\data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# visit use read mode
with open(r"Library\data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
