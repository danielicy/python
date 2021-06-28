import random
import string
print(random.random())
print(random.randint(1, 10))
# picks a random number from list
print(random.choice([1, 5, 8, 10, 12]))
# picks 2 random numbers from list
print(random.choices([1, 5, 8, 10, 12], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)
