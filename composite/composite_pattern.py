from __future__ import annotations
from abc import ABC, abstractmethod 
from typing import List

class Component(ABC):
    """
    The Component class declares common operations for both simple and
    complex objects of a composition 
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods. 
        """
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that let the client code figure out whether a 
        component can bear children.
        """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to 
        concrete classes (by declaring the method containing the behavior as
        "abstract") 
        """

class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A Leaf can't 
    have any children

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    """
    The Composite class represent the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their 
    children and then "sum-up" the result 
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    
    """
    A composite boject can add or remove other components (both simple or
    complex)  to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self)-> str:
        """
        The composite executes its primary logic in a particular way.
        It traverse recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
    
def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface. 
    """
    print(f"Result:{component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}", end="")

if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")


    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a compoiste tree:")
    client_code(tree)
    print("\n")

    print("Client : I don't need to check the compoents classes even when managing the tree:")
    client_code2(tree, simple)

