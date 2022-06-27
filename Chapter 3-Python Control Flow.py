# program ask user's name
# program checks if the user has more than or equal to $30
name = input("Enter your name: ")
money = input("Enetr your cash amount: ")
hungry = input("Are you hungry? (Y/N) ")

print("Your name is " + name)
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

for a, b,c in [(1, 2, 4), (3, 5, 6), (5, 7, 9)]:
    print(a + b + c)

# ditionary (key)
myDictionary = {"name": "Ray", "age": 27}
for key,value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")


# While loop
x = 0
while x < 1000000000:
    # print(x)
    x += 1  # we must write this line of code
print(x)

s = 0
for i in range(1000000000):
    s += 1
print(s)


counter = 0  # 計次
for i in "123":
    for j in "abc":
        print(i, j)
        counter += 1
print(f"counter is now {counter}")

# Pass
for i in range(1000000000000):
    # some codes go here
    pass

# Break
for i in "123456789":
    if i == "5":
        break
    else:
        print(i)


# function
for i in [1,2,3,4,5,6,7,8,9,10,]:
    print(i)

for i in "1234":
    for j in "abcd":
        if j == "c":
            break
        else:
            print(i, j)

# continue
for i in "ABCDE":
    if i == "B":
        continue
        print(i)
    print(i)


# range
for i in range(20, 15, -1):  # range() function returns an iterable object
    print(i)

# typecasting to list
mylist = list(range(0, 15, 2))
print(mylist)


print(range(5))


# Enumerate
counter = 0
for letter in "Hello world":
    if counter < 10:
        print(letter)
    counter += 1

for counter, char in enumerate("Hello world"):
    if counter < 10:
        print(char)


# zip
x = [1, 2, 3]
y = ['A', 'B', 'C']
z = ['a', 'b']

for tuple in zip(x, y, z):
    print(tuple)

# comprehension
x = [1,2,3,4]
# squared_x = [1,,4,9,16]
squared_x = []
for item in x:
    squared_x.append(item ** 2)
print(squared_x)

# list comprehension
x = [1,2,3,4]
squared_x = [item ** 2 for item in x if item > 2]
print(squared_x)

# dictionary comprehension
x = [1,2,3,4]
x_squared_dict = {item: item**2 for item in x if item > 2}
print(x_squared_dict)


# set
x = [1,2,4,3]
x_squared_set = {item**2 for item in x if item > 2}
print(x_squared_set)


# generator
x = [1,2,3,4]
x_squared_generator = (item ** 2 for item in x)
print(x_squared_generator)

for i in x_squared_generator:
    print(i)


from sys import argv
if len(argv) < 2:
    print("Please provide a filename.")
else:
    file = open(argv[1])
    lines = file.read()

    lines = lines.split("\n") # a list of strings
    word_count = 0
    letter_count = 0

    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    line_count = len(lines) - 1

    print(f"The line count is{line_count}")
    print(f"The word count is{line_count}")
    print(f"The letter count is{line_count}")

#tuple((i for i in (1, 2, 3)))
