class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __iter__(self):
        return iter(self._children)

    def __repr__(self):
        return 'repr Node({!r})'.format(self._value) # diffrent between __repr__ and __str__ https://stackoverflow.com/questions/38418070/what-does-r-do-in-str-and-repr

    # def __str__(self):
    #     return 'str Node({!s})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)


# next（参数）