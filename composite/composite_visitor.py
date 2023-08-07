from abc import ABC, abstractmethod
from typing import List

class Operation(ABC):
    @abstractmethod
    def accept(self, visitor : Visitor) -> None:
        return

class File(Operation):
    def __init__(self, name : str, size :int):
        self.name = name
        self.size = size

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_file(self)

    def fileInfo(self) -> str:
        return "file name: " + self.name + ", file size : " + str(self.size)

class Directory(Operation):
    def __init__(self, name) -> None:
        self.name = name
        self.children : List[Operation] = []

    def attach(self, operation : Operation) -> None:
        self.children.append(operation)
    def remove(self, operation : Operation) -> None:
        self.children.remove(operation)

    def directoryInfo(self) -> str:
        return "Directory name " + self.name

    def getChildrenInfo(self) -> List[Operation]:
        return self.children

class Visitor(ABC):
    @abstractmethod
    def visit_file(self, operation : Operation) ->None:
        pass

    @abstractmethod
    def visit_directory(self, operation : Operation) -> None:
        pass

class DashVisitor(Visitor):
    def visit_file(self, operation: Operation) -> None:
        operation.fileInfo()
    def visit_directory(self, operation : Operation) -> None:
        operation.directoryInfo()


d = Directory("root")
d1 = Directory("Duck")
d2 = Directory("Rabbit")
d.attach(d1)
d.attach(d2)

d1.attach(File("duck1", 100))
d1.attach(File("duck2", 20))
d1.attach(File("duck3", 700))

d2.attach(File("rabbit1", 11))
d2.attach(File("rabbit2", 22))


