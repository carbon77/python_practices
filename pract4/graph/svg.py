class Shape:
    def print(self) -> str:
        pass


class Circle(Shape):
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def print(self) -> str:
        return f'<circle cx="{self.x}" cy="{self.y}" r="{self.r}" fill="{self.color}" />'


class Line(Shape):
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

    def print(self) -> str:
        return f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.color}" />'


class Text(Shape):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def print(self) -> str:
        return f'<text x="{self.x}" y="{self.y}" fill="white" font-size="10px">{self.text}</text>'


class SVG:
    def __init__(self):
        self.children = []

    def line(self, x1, y1, x2, y2, color):
        self.children.append(Line(x1, y1, x2, y2, color))

    def circle(self, x, y, r, color):
        self.children.append(Circle(x, y, r, color))

    def text(self, x, y, text):
        self.children.append(Text(x, y, text))

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write(f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')

            for child in self.children:
                f.write('\n' + child.print())

            f.write('\n</svg>')


if __name__ == '__main__':
    svg = SVG()

    svg.line(10, 10, 60, 10, color='black')
    svg.line(60, 10, 60, 60, color='black')
    svg.line(60, 60, 10, 60, color='black')
    svg.line(10, 60, 10, 10, color='black')
    svg.line(40, 10, 30, 100, color='green')

    svg.circle(10, 10, r=5, color='red')
    svg.circle(60, 10, r=5, color='red')
    svg.circle(60, 60, r=5, color='red')
    svg.circle(10, 60, r=5, color='red')

    svg.save('pic.svg', 100, 100)
