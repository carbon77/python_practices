from queue import Queue

from pract4.graph.svg import SVG


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Tree = left
        self.right: Tree = right
        self.x = 0
        self.y = 0
        self.scale_x = 30
        self.scale_y = 50

    def init_cords(self, x_left=0.0, y=0):
        self.y = y

        if self.left is None and self.right is None:
            self.x = x_left
            return self.x, self.x

        if self.left is not None and self.right is not None:
            right_of_left, left_x = self.left.init_cords(x_left, self.y + 1)
            right_of_right, right_x = self.right.init_cords(right_of_left + self.scale_x, self.y + 1)
            self.x = left_x + (right_x - left_x) / 2
            return right_of_right, self.x

        if self.left is not None:
            right, left_x = self.left.init_cords(x_left, self.y + 1)
            self.x = left_x
            return right, self.x

        if self.right is not None:
            right, right_x = self.right.init_cords(x_left, self.y + 1)
            self.x = right_x
            return right, self.x

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

            if current_node.left is not None:
                left_x = current_node.left.x + 10
                left_y = current_node.left.y * self.scale_y + 10
                svg.line(current_x, current_y, left_x, left_y, 'black')
                stack.put(current_node.left)

            if current_node.right is not None:
                right_x = current_node.right.x + 10
                right_y = current_node.right.y * self.scale_y + 10
                svg.line(current_x, current_y, right_x, right_y, 'black')
                stack.put(current_node.right)

        svg.save(filename, width + 10, height + 10)


if __name__ == '__main__':
    tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
    tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
    tree = Tree(1, tree_2, tree_8)
    tree.print('tree1.svg')
