# # # # # FUNCTION RECAP:


# Two key word arguments -- kwargs.
def inventory(**inv):
    for k, v in inv.items():
        print("{} is {}".format(k, v))


inventory(feather=2, socks=4, bread=1)


# How to use returned data: assign it to a variable.
def modulo(num):
    return num % 2


data = modulo(40)
print(data)


# # # # # LAMBDAS:


# Lambda is used to quickly define a function. It is commonly used with built-in functions filter and map.
multiply = lambda x, y: x * y
print(multiply(11, 3))

# Filter function filters a list according to an expression -- filter(expression, listName):
# The expression must return true or false.
myList = [23, 45, 66, 72, 89]


def odd_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


newList = filter(odd_numbers, myList)
print(list(newList))

# Now we can do it with a lambda, WAY quicker.
newLambdaList = filter(lambda x: x % 2 == 0, myList)
# The : between x is shorthand for an if statement.
print(list(newLambdaList))

# Map function performs quick functions on numbers in a list. Like a faster for loop.
newMappedList = map(lambda x: x * 2, myList)
print(list(newMappedList))


# # # # # NAME = MAIN:


# Instead of while true: during the assessment, clean it up with this.
def game():
    print(5 + 6)
    # Literally all game code goes here.


if __name__ == "__game__":
    game()


# # # # # IMPORTING:


# Should use different scripts (modules) for the assessment, e.g. one for all room descriptions.
# Now to access data from the other script.
import roomDescriptions  # This should really be at the very top of the file.
print(roomDescriptions.room1["Description"])

### You could name it shorter with:
# import roomDescriptions as rd
# print(rd.room1["Description"])

### Alternatively:
# from roomDescriptions import room1
### Now you could do:
# print(room1["Description"])

# from roomDescriptions import *
### This means import ALL variables from roomDescriptions

# Random number function.
import random

print(random.randint(2, 10))  # Random int.
print(random.uniform(3.5, 5))  # Random float.
print(random.choice(["Bunny", "Big bunny", "MASSIVE bunny"]))  # Picks one of these. Can be used with lists/dicts.
