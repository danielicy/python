import sys
from modules.ecomerce.shopping import sales
from dcpdf import pdf2image, pdf2txt


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user)
    pdf2txt.convert()


letters = ['a', 'b', 'c', 'd']
zeros = [0] * 5
combined = zeros + letters
enumaration = list(range(20))

numbers = [1, 2, 3, 4]
first, second, *other = numbers
uno, *otros, penultimo, ultimo = enumaration

save_user(id=1, name="john", age=22)
print(multiply(2, 3, 4, 5))
print(combined)
print(uno, otros, penultimo, ultimo)

for letter in enumerate(letters):
    print(letter)

letters.pop(0)
letters.remove("b")
del letters[0]
letters.clear()


items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# is the same as:

items.sort(key=lambda item: item[1])

# -------------------------------

prices = []
for item in items:
    prices.append(item[1])

# is the same as:

prices1 = list(map(lambda item: item[1], items))
# same as:
prices2 = [item[1] for item in items]


filtered = list(filter(lambda item: item[1] >= 10, items))
# is the same as:(comprehesion)
filtered = [item for item in items if item[1] >= 10]
print(filtered)


print(sys.path)

print(dir(sales))
