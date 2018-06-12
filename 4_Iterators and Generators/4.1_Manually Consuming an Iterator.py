filePath = '/Users/wankun/Desktop/PyWorkspace/pyCookBook/4_Iterators and Generators/testFile'
filePath2 = '/Users/wankun/Desktop/PyWorkspace/pyCookBook/4_Iterators and Generators/testFile2'

# use next function and catch stopIteration exception
with open(filePath) as f:
    try:
        while True:
            line = next(f)
            print(line, end='')

    except StopIteration:
        pass


# use terminat value
with open(filePath) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1, 2, 3]
it = iter(items)# get the iterator, items.__iter__()
next(it) # run the iterator , it.__next__()
next(it)
next(it)
# next(it) # StopIteration



# print args
# print(*objects, sep=' ', end='\n', file=sys.stdout)
print('abc', 123, sep=' *** ', end=' !!!', file=open(filePath2, 'w'))

