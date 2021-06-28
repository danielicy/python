point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]

values = []
for x in range(5):
    values.append(x*2)

values = [x * 2 for x in range(5)]


valuesdictionary = {x: x * 2 for x in range(5)}
print(valuesdictionary)

print(valuesdictionary[1])
