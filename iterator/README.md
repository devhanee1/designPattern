# Intent
Iterator is a behavioral design pattern that lets you traverse element of a collection without exposing its underlying represent(list, stack, tree, etc...)

# Problem
Collection - one of the most used data types in programming. 
Most collections store their elements in simple lists. However, some of them are based on stacks, trees, graphs and other complex data structure. 

But no matter how a collection is structured, it must provide some way of accessing its elements so that other code can use these element.
There should be a way to go through each element of the collection without accessing the same elements over and over. 

![image](https://github.com/devhanee1/designPattern/assets/37257706/120bc7c4-a1cb-4da1-90db-02d88c12b645)
- There are not only list for traversal.
- There are many data structure and also there are many ways to traversal.
- If iterator code is fixed in some way, there will be much cost to modify it with another way.

> How do you sequentially traverse elements of a complex data structure, such as a tree?

> Adding more and more traversal algorithms to the collection gradually blurs its primary responsibility, which is efficient data storage.

# Solution
The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an iterator. 

![image](https://github.com/devhanee1/designPattern/assets/37257706/46c3a7ae-fe04-417f-9967-f9f6580d2082)
- iterator implement various traversal algorithms. Several iterator objects can traverse the same collection at the same time.

In addtional to implementing the algorithm itself, an iterator object encapsulates all of the traversal details, such as the current position
and how many elements are left till the end. Because of this, several iterators can go through the same collection at the same time, independently
of each other. 

All iterators must implement the same interface. This makes the client code compatible with any collection type of any traversal algorithm
as long as there's a proper iterator. 

# Structure
![image](https://github.com/devhanee1/designPattern/assets/37257706/71f59d91-d8d9-46c3-820c-ead3273d3ac9)

## Iterator
interface declares the operations required for traversing a collection : Fetching the next element, retrieving the current position, restarting iteration, etc.

## Concrete Iterators
Implement specific algorithms for traversing a collection. 

## Collection
Interface declares one of multiple methods for getting iterators compatible with the collection.
Return type of the methods must be declared as the iterator interface so that the concrete collection can return various kind of iterators. 


# How to Implement
1. Declare the iterator interface : fetch the next element 
2. Declare collection interface : return iterator interface. 
3. Implement concrete iterator classes for the collections that you want to be traversable with iterator. -> 여기서 iterator object 는 single collection instance 와 반드시 연결이 되어 있어야 함. 보통 그 링크는 생성자에서 연결됨. 실은 이 부분이 가장 Main. 즉 iterator 란 wrapper 를 만드는 것이고, 실제 iterator 로직을 여기서 다 만드는 듯함. 즉 collection 의 일종의 traversal wrapper 라고 볼 수 있으니 main code 는 여기에 집중이 되어 있어야 함. 
4. Implement the collection interface in your collection classes. 여기서 collection object 는 반드시 스스로 그 instance 를 iterator' constructor 에 넘겨야 한다. link 를 생성하기 위해서. 

# Relations with other patterns
1. You can use Iterator to traverse Composite trees.
2. You can use Factory Method along with Iterator to let collection subclasses return different types of iterators that are compatible with the collections.
3. You can use Visitor along with Iterator to traverse a complex data structure and execute some operation over its elements, even if they all have different classes. 
