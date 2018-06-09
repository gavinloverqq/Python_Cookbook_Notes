grades = [1, 3, 4, 5, 6, 7, 10]


def avg(data):
    sequence = [float(item) for item in data]
    if len(sequence) < 1:
        return None
    else:
        return sum(sequence) / len(sequence)

print(avg(grades))


def dropFirstLast(grades):
    first, *mid, last = grades # start expressions can be used of arbitrary length
    return avg(mid)

print(dropFirstLast(grades))



# sequence of tuple of varying length

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print("bar", s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# string processing
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *filelds, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# ignore something or throwaway something
records = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = records
print(name)
print(year)

# carry out recursive algorithm
item = [1, 10, 7, 4, 5, 9]
def sumrec(item):
    head, *tail = item
    return head + sumrec(tail) if tail else head


# The pythonic way to do it is from the PEP 8 style guide (where Yes means “recommended” and No means “not recommended”):
#
# For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
#
# Yes: if not seq:
#      if seq:
#
# No:  if len(seq):
#      if not len(seq):


print(sumrec(item))



