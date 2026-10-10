"""The and operator returns True if both operands are True, and False otherwise."""
test = True and True
print(test)
test = True and False
print(test)
test = False and False
print(test)
test = False and True
print(test)

"""The or operator returns True if either or both operands are True, and False otherwise."""

test = True or True
print(test)
test = True or False
print(test)
test = False or False
print(test)
test = False or True
print(test)

"""The not operator returns the opposite of the operand, e.g. not True gives False."""

test = True or True and False, False or False and True, (True and False) or (False and True), (True or False) and (False or True)
print(test)