from abc import ABC, abstractmethod
from typing import List

class FileOperation(ABC):
    @abstractmethod
    def getSize(self) -> int:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def printInfo(self) -> None:
        pass

    def isDirectory(self) -> bool:
        return False

class Directory(FileOperation):
    def __init__(self, name:str):
        self._children : List[FileOperation] = []
        self._name = name

    def getName(self) -> str:
        return self._name

    def getSize(self) -> int:
        sizeSum = 0
        for child in self._children:
            sizeSum += child.getSize()
        return sizeSum

    def printInfo(self) -> None:
        print(self.getName() , ", ", str(self.getSize()))
        for child in self._children:
            child.printInfo()

    def add(self, file:FileOperation) -> None:
        self._children.append(file)

    def remove(self, file:FileOperation) -> None:
        self._children.remove(file)

    def isDirectory(self) -> bool:
        return True

class File(FileOperation):
    def __init__(self, name:str, size:int):
        self._size = size
        self._name = name 

    def getName(self) -> str:
        return self._name 

    def getSize(self) -> int:
        return self._size

    def printInfo(self) -> None:
        print(self.getName(), ", " , str(self.getSize()))

sport = Directory("sport")
sport.add(File("baseball", 100))
sport.add(File("soccer", 300))
sport.add(File("basketball", 40))

food = Directory("food")
food.add(File("pizza", 1000))
food.add(File("soda", 2000))

root = Directory("root")
root.add(sport)
root.add(food)

print(root.getSize())
print("------")
root.printInfo()
