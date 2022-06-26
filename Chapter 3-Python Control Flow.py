# program ask user's name
# program checks if the user has more than or equal to $30
name = input("Enter your name: ")
money = input("Enetr your cash amount: ")
hungry = input("Are you hungry? (Y/N) ")

if hungry == "Y":
    if int(money) >= 30:
        print(f"{name} should go to eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to buy breakfast.")
elif hungry == "N":
    if int(money) >= 30:
        print(f"{name} has bought but doesn't want to eat breakfast.")
    else:
        print(f"{name} has no money but is not hungry..")
else:
    print("Please make sure that you enter either Y or N.")

# For and While Loop
# for variable in iterable:
#     do something here
for letter in "Hello World":
    if (letter == letter.upper()):
        print(letter)

myList = [1, 3, 5, 7, 9]
for num in myList:
    print(num)

# a list of tuples
for tuple in [(1, 2), (3, 5), (5, 7)]:
    print(tuple)

for a, b in [(1, 2), (3, 5), (5, 7)]:
    print(a + b)

# ditionary (key)
myDictionary = {"name": "Ray", "age": 27}
for key, value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")


# While loop
