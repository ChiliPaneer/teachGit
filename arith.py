def add(n, m):
    return n + m

def multiply(n, m):
    return n*m

def subtract(n, m):
    return n - m

def divide(n,m):
    return n/m 

# Testing

x = add(4,5)
print("4 + 5 =", x)
if (x == 9):
    print("Working!")
else:
    print("ERROR!")

x = multiply(4,5)
print("4 * 5 =", x)
if (x == 20):
    print("Working!")
else:
    print("ERROR!")
    
x = subtract(4,5)
print("4 - 5 =", x)
if (x == -1):
    print("Working!")
else:
    print("ERROR!")
    
x = divide(10,5)
print("10 / 5 =", x)
if (x == 2):
    print("Working!")
else:
    print("ERROR!")
