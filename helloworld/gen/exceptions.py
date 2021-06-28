try:
    file = open("app.py")
    age = int(input("Age"))
except ValueError as ex:
    print("Invalid age")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age can't be 0")
except (TypeError, SyntaxError):
    print("mmmm......something went wrong")
else:
    print("no exceptions where thrown")
finally:
    file.close()
print("Execution continues")


try:
    with open("app.py") as file, open("array.py") as target:
        print("File oppened")
    age = int(input("Age"))
except ValueError as ex:
    print("Invalid age")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age can't be 0")
except (TypeError, SyntaxError):
    print("mmmm......something went wrong")
else:
    print("no exceptions where thrown")
print("Execution continues")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age
