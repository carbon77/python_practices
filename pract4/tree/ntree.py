from queue import Queue

from pract4.tree.svg import SVG


class Tree:
    def __init__(self, val, *nodes):
        self.val = val
        self.nodes = nodes
        self.x = 0
        self.y = 0
        self.scale_x = 30
        self.scale_y = 50

    def init_cords(self, x_left=0.0, y=0):
        self.y = y

        if len(self.nodes) == 0:
            self.x = x_left
            return self.x, self.x

        rights = [x_left]
        child_xs = []

        for node in self.nodes:
            next_right = rights[-1]

            if node != self.nodes[0]:
                next_right += self.scale_x

            right, child_x = node.init_cords(next_right, self.y + 1)
            rights.append(right)
            child_xs.append(child_x)

        if len(child_xs) == 1:
            self.x = child_xs[0]
        else:
            self.x = child_xs[0] + (child_xs[-1] - child_xs[0]) / 2

        return rights[-1], self.x

    def print(self, filename):
        svg = SVG()
        stack = Queue()
        stack.put(self)
        height = 0
        width = 0
        tree.init_cords()

        while not stack.empty():
            current_node = stack.get()
            current_x = current_node.x + 10
            current_y = current_node.y * self.scale_y + 10
            width = max(width, current_x)
            height = max(height, current_y)
            svg.circle(current_x, current_y, 5, 'black')

            for node in current_node.nodes:
                x = node.x + 10
                y = node.y * self.scale_y + 10
                svg.line(current_x, current_y, x, y, 'black')
                stack.put(node)

        svg.save(filename, width + 10, height + 10)


if __name__ == '__main__':
    tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
    tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
    tree_1 = Tree(1, tree_2, tree_8)
    tree = Tree(1, tree_1, Tree(3, Tree(1, Tree(1, Tree(2), Tree(1), Tree(5)))), Tree(1, Tree(3), Tree(3)))
    # tree = Tree(1, tree_1, Tree(1, Tree(1, Tree(1, Tree(1, Tree(1, Tree(1, Tree(1))))))))
    tree.print('tree2.svg')
