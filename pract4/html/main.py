class Element:
    def __init__(self):
        self.parent: Tag = None

    def get_code(self, indent=0) -> str:
        pass


class TextElement(Element):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def get_code(self, indent=0) -> str:
        return " " * indent + self.value


class Tag(Element):
    def __init__(self):
        super().__init__()
        self.children: list[Element] = []
        self.name = ''

    def append(self, child: Element):
        child.parent = self
        self.children.append(child)

    def get_code(self, indent=0):
        code = f'{" " * indent}<{self.name}>\n'

        for child in self.children:
            code += f'{child.get_code(indent + 1)}\n'

        return code + " " * indent + f'</{self.name}>'


class Body(Tag):
    def __init__(self):
        super().__init__()
        self.name = 'body'


class Div(Tag):
    def __init__(self):
        super().__init__()
        self.name = 'div'


class Paragraph(Tag):
    def __init__(self):
        super().__init__()
        self.name = 'p'


class HTML:
    def __init__(self):
        self.head: Tag = None
        self.current: Tag = None

    def get_code(self):
        return self.head.get_code()

    def template_method(self, tag):
        if self.head is None:
            self.head = tag
        else:
            self.current.append(tag)

        self.current = tag
        return self

    def body(self):
        return self.template_method(Body())

    def div(self):
        return self.template_method(Div())

    def p(self, text):
        tag = Paragraph()
        tag.append(TextElement(text))
        self.current.append(tag)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current = self.current.parent


if __name__ == '__main__':
    html = HTML()

    with html.body():
        with html.div():
            with html.div():
                html.p("First line")
                html.p("Second line")

                with html.div():
                    html.p("First line")
                    html.p("Second line")

            with html.div():
                html.p("Third line")

    print(html.get_code())
