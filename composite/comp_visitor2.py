
from abc import ABC, abstractmethod
from typing import List

class Operation(ABC):
    def add():
        pass

    def remove ():
        pass

    def is_compoiste():
        return False

    def getChildren():
        pass

    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def getSize():
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class File(Operation):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def accept(self, visitor):
        visitor.visit_file(self)
        

class Directory(Operation):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, operation):
        self.children.append(operation)
    
    def remove(self, operation):
        self.children.remove(operation)

    def getChildren(self):
        return self.children

    def getName(self):
        return self.name
    
    def getsize(self):
        return 0

    def accept(self, visitor):
        visitor.visit_directory(self)

class Visitor(ABC):
    @abstractmethod
    def visit_file(self, f):
        pass 

    @abstractmethod
    def visit_directory(self, d):
        pass

class DashVisitor(Visitor):
    def visit_file(self, f):
        print("-----------------------")
        print(f.getName() + str(f.getSize()))
    
    def visit_directory(self, d):
        print("-----------------------")
        print(d.getName())