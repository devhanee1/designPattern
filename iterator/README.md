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


