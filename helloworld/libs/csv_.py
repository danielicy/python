import csv
from os import read

# to create:
with open("helloworld/data/data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 250, 5])
    writer.writerow([1001, 251, 10])


# to open
with open("helloworld/data/data.csv") as dfile:
    reader = csv.reader(dfile)
    for row in reader:
        print(row)
