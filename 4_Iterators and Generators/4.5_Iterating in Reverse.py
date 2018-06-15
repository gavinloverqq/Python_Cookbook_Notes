a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# size of implements a __reversed__() method can be reversed, if
# neither of these can be satisfied, you will convert the object into a list first

f = open("testFile")
for x in reversed(list(f)):
    print(x)