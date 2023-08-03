from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    The context defines the interface of interests to client. 
    It also maintains a reference to an instance of a State subclass, which represents 
    the current state of the Context. 
    """
    _state = None

    def __init__(self, state: State) -> None:
        self.transition(state)
    def transition(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its hehavior to the current State Object
    """
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backrefernce to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another state.
    """
    @property
    def context(self) -> context:
        return self._context

    @context.setter
    def context(self, context:Context) -> None:
        self._context = context 

    def handle1(self) -> None:
        pass
    def handle2(self) -> None:
        pass

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handle request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition(ConcreteStateB())
    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition(ConcreteStateA())

if __name__ == "__main__":

    context = Context(ConcreteStateA())

    context.request1()
    context.request1()
    context.request2()
    context.request1()
