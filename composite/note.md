# Definition

Composite is a structure design pattern that lets you compose objects into tree
structures and then work with these structures as if they were individual objects

- Structure design pattern

# Problem
Using the Composite pattern makes sense only when the core model of your app can be
repsesented as a __tree__.

For example, imagine that you have two types of objects: Product and Boxes. A Box can
contain several Products as well as a number of smaller Boxes. These little Boxes can
also hold some Products or even smaller Boxes and so on.

![image](https://github.com/devhanee1/designPattern/assets/37257706/25ee3c45-6bd4-415d-9a65-59c2e724b5b6)



# Solution
The Composite pattern suggests that you work with Product and Boxes through a common interface 
which declares a method for calculating the total price. 

How would this method works? For a product, it'd simple return the product's price. For a box,
it'd go over each item the box contains, ask its price and then return a total for this box.
If one of these itmes were a smaller box, that box would also start going over its contents and so on,
until the prices of all inner components were calculated. A Box could even add some extra cost to 
the final price, such as packaging cost.

The greatest benefit of this approach is that you don't need to care about the concrete classes of
objects that compose the tree. You don't need to know whether an object is a simple product or a
sophisticated box. You can treat them all the same via the common interface. When you call a method,
the objects themselves pass the request down the tree. 

# Structure
![image](https://github.com/devhanee1/designPattern/assets/37257706/b44f6641-d0ab-43b9-b976-326e6819a179)

## Component
The Component interface describes operations that are common to both simple and complex elements of the tree

## Leaf
The Leaf is a basic element of a tree that doesn't have sub-elements. 

## Container
The Container(aks composite) is an element that has sub-elements: leaves or other containers. 
A container doesn't know the concrete classes of this children. It works with all sub-elements only 
via the component interface. 

## Client
The client works with all elements through the component interface. As a result, the client can work in the
same way with both simple or complex elements of the tree.

# Pseudocode
![image](https://github.com/devhanee1/designPattern/assets/37257706/b7f28b96-96e9-4224-84e7-04e7dda92a16)

```
// The component interface declares common operations for both
// simple and complex objects of a composition.

interface Graphic is
  method move(x,y)
  method draw()

class Dot implements Graphic is
  field x, y

  constructor Dot(x, y) {...}
  method move(x, y) is
    this.x += x, this.py += y
  method draw() is
    // draw a dot at X and Y

class Circle extends Dot is
  field radius
  constructor Circle(x, y, radius) {...}

class CompoundGraphic implements Graphc is
  field children: array of Graphic

  method add(child : Graphic) is
    // Add a child to the array of children

  method remove(child : Graphic) is
  // Remove a  child reom the array of children

  method move(x, y) is
    foreach (child in children) do
      child.move(x, y)
  method draw() is
    for each child compoent:
      draw the componet

class ImageEditor is
    field all :CompundGraphic

    method load() is
      all = new CompoundGraphic()
      all.add(new Dot(1,2))
      all.add(new Circle(5, 3, 10))

    method gourpSelected(components: array of Graphic) is
      group =new CompoundGraphic()
      foreach (component in components) do
        groupd.add(compoent)
        all.remove(component)
      all.add(group)
      all.draw()

  

```


