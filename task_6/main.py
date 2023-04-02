class Node:
    def __init__(self, value, enter_value, children=None):
        self.value = value
        self.enter_value = enter_value
        self.children = children


def main(args):
    tree = init_tree()
    current_node = tree

    while current_node.children is not None:
        arg = args[current_node.value]

        for child in current_node.children:
            if arg == child.enter_value:
                current_node = child

    return current_node.value


def init_tree():
    return Node(3, None, [
        Node(4, 1989),
        Node(1, 1984, [
            Node(2, 'PIKE', [
                Node(5, 'SCSS'),
                Node(6, 'HACK')
            ]),
            Node(0, 'GDB', [
                Node(7, 2016),
                Node(8, 2017)
            ]),
            Node(9, 'FLUX')
        ]),
        Node(2, 1960, [
            Node(3, 'HACK'),
            Node(1, 'SCSS', [
                Node(0, 'PIKE'),
                Node(1, 'GDB'),
                Node(2, 'FLUX')
            ])
        ])
    ])


print(main([2016, 'GDB', 'SCSS', 1960]))
print(main([2017, 'GDB', 'HACK', 1989]))
print(main([2017, 'FLUX', 'HACK', 1960]))
print(main([2017, 'GDB', 'HACK', 1984]))
print(main([2016, 'GDB', 'HACK', 1984]))
