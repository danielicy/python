numbers = [1, 1, 2, 3, 4, 4, 5]
uniques = set(numbers)

second = {1, 5}
combined = (numbers | second)
print(combined)
mutual = numbers & second
print(mutual)
diff = numbers - second
print(diff)
either = (numbers ^ second)
print(either)
