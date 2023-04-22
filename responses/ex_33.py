c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())
# it will print out a 3 anytime you call the function c will be overwritten