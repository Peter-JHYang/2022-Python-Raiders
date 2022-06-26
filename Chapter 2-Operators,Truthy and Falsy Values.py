# Comparison and Assignment Operators
from audioop import reverse


a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

c = "today is a good day."
print(c == c.lower())


def math(index, a, b):
    if index == 1:
        a += b
    elif index == 2:
        a -= b
    elif index == 3:
        a *= b
    elif index == 4:
        a /= b
    else:
        a **= b
    print(a)


a = 10
b = 20
math(1, a, b)
math(2, a, b)
math(3, a, b)
math(4, a, b)
math(5, a, b)


# Logical and Bitwise Operators

# Truthy and Falsy Values


# Short-Circuit Evaluation
