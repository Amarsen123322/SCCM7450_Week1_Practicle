x = 3
#print(x, type(x)) # types tell you what is it here 3 is an int
# print(x + 1) # Addition
# print(x - 1) # Subtraction
# print(x * 2) # Multiplication
## print(x ** 2) # Exponentiation

# x += 1
# print(x)
# x *= 2
# print(x)

# y = 2.5
# print(type(y))
# print(y, y + 1, y * 2, y ** 2)

# t, f = True, False
# print(type(t))
# print(t and f) # Logical AND;
# print(t or f) # Logical OR;
# print(not t) # Logical NOT;
# print(t != f) # Logical XOR;

# xs = [3, 1, 2] # Create a list
# print(xs)

# t = (1, 2, 3,4,5,6) # Tuples are created using round brackets - ()
# print(t[0]) # Access the first element by index
# print(t[1:4]) # Tuples can also be sliced similar to lists

d = {(x, x + 1): x for x in range(10)} # Create a dictionary with tuple keys
print(d)
t = (5, 6) # Create a tuple
print(type(t))
print(d[t])
print(d[(1, 2)])