wallet = 200
print(wallet + 100)
print(wallet - 100)
print(wallet * 2)
print(wallet / 2)
print(wallet % 5)
print(wallet ** 2)


name = "Peter Hung"
print(name.replace("Hung","Yang"))


sentence = "Hi, Hello, Amy"
print(sentence.split(","))

print(list(sentence))


print("I have a string {}".format("Hi ,I'm OK."))

print("{name}, {address}, {age}".format(name = "Ray", age = 10, address="Touyuan"))


#fstring
myName = "Ray"
age = 18
print(f"Hello, my name is {myName}, I am {age} years old.")


luckyNumber = [2,3,4,5,6,7,8,9]
print(luckyNumber[::-1])  #[9, 8, 7, 6, 5, 4, 3, 2]

print(luckyNumber[:-1])  #[2, 3, 4, 5, 6, 7, 8]


x = [1,3,8,1,2,7,5]
y = x.copy()
y[0] = 15
print(x)
print(y)


x = 25
y = 35
x,y = y,x
print(x)
print(y)

#type check
x = [1,2,3,4,5]
print(type(x))

def hello():
    print("hello")
hello()

#join 
myList = ["a","b","c","d"]
mystring = ",".join(myList)
print(mystring)

#sort 
x = [4,2,3,1]
y = sorted(x)
print(x)
print(y)

