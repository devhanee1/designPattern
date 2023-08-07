
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List 

class Operation(ABC):
    @property
    def parent(self) -> Operation:
        return self._parent

    @parent.setter
    def parent(self, parent : Operation) -> None:
        self._parent = parent   


    def add(self, o:Operation) -> None:
        pass

    def remove(self, o:Operation) -> None:
        pass

    @abstractmethod
    def accept(visitor : Visitor): 
        pass

    @abstractmethod
    def getSize() -> int:
        pass

class File(Operation):
    def __init__(self, name, size):
        self.name = name
        self.size = size 

    def accept(self, visitor : Visitor):
        visitor.visit_file(self)
    
    def showFileInformation(self):
        print("File name ", self.name, ", File size:", self.getSize())

    def getSize(self) -> int:
        return self.size

class Directory(Operation):
    def __init__(self, name):
        self.name = name
        self.children : List[Operation] = []

    def accept(self, visitor : Visitor):
        visitor.visit_directory(self)

        for c in self.children:
            c.accept(visitor)

    def showDirectoryInformation(self):
        print("Directory name:" , self.name, "size:", self.getSize())

    def add(self, o:Operation) -> None:
        self.children.append(o)
    
    def remove(self, o:Operation) -> None:
        self.children.remove(o)

    def getSize(self) -> int:
        size = 0
        for c in self.children:
            size += c.getSize()
        return size

class Visitor(ABC):
    @abstractmethod
    def visit_file(self, f : File):
        pass

    @abstractmethod
    def visit_directory(self,d: Directory):
        pass

class VisitorSimple(Visitor):
    def visit_file(self, f : File):
        print("--------")
        f.showFileInformation()

    def visit_directory(self,d: Directory):
        print("--------")
        d.showDirectoryInformation()

class VisitorStar(Visitor):
    def visit_file(self, f : File):
        print("*********")
        f.showFileInformation()

    def visit_directory(self,d: Directory):
        print("**********")
        d.showDirectoryInformation()



r = Directory("root")
d1 = Directory("Dir1")
d1.add(File("file001", 10))
d1.add(File("file002", 15))

d2 = Directory("Dir2")
d2.add(File("file00000001", 110000))
d2.add(File("file00000002", 510000))

r.add(d1)
r.add(d2)

visitor = VisitorSimple()
visitor2 = VisitorStar()
r.accept(visitor)
r.accept(visitor2)

