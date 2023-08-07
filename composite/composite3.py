"""
The Composite pattern is pretty common in Python code. It's open used to represent
hierarchies of user interface. 

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List 

class Component(ABC):
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

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    boject tree assemply. The downside is that these methods will be empty for
    the leaf-level components. 
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component:Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self)->str:
        pass


class Leaf(Component):
    def operation(self)->str:
        return "Leaf"

class Composite(Component):
    def __init__(self) -> None:
        self._children : List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their resutls. Since the composite's children pass these call to their
        children and so forth, the whole object tree is traversed as a result 
        """
        result = []
        for c in self._children:
            result.append(c.operation())
        return f"Branch({'+'.join(result)})"

def client_code1(component:Component) -> None:
    print(f"Result : {component.operation()}", end ="")


def client_code2(component1:Component, component2:Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Result:{component1.operation()}", end ="")

if __name__ == "__main__":
    simple = Leaf()
    client_code1(simple)
    print("\n")


    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    client_code1(tree)