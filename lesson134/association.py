# Relationships between classes: association, aggregation, and composition
# Association is a type of relationship where objects
# are linked inside the system.
# This is the most common relationship between objects and has subsets
# like aggregation and composition (which we will see later).
# Generally, we have an association when one object has
# an attribute that references another object.
# The association does not specify how one object controls
# the lifecycle of another object.
class Writer:
    def __init__(self, name) -> None:
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing'


writer = Writer('Luiz')
pen = WritingTool('Bic Pen')
typewriter = WritingTool('Typewriter')
writer.tool = typewriter

print(pen.write())
print(typewriter.write())
print(writer.tool.write())
