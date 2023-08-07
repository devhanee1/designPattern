# Visitor
- Visitor is behavior design pattern that lets you separate algorithms from the objects on which they operate.

# Problem
- Image developing an app which works with geographic information structured as one colossal graph.
- Each node of the graph may represent a complex entity such as a city, but also more granular thing like industries, sightseeing areas, etc.
- The nodes are connected with others if there's a road bwtween the real objects that they represent.
- Under the hood, each node type is represneted by its own class, while each specific node is an object
<hr>

- At some point, you got a task to implement exporting the graph into XML format.
- The job seemed pretty straightforward. You planned to add an export method to each node class and then leverage recursion to go over each node of the graph.
- But, Unfortunately, the system architect refused to allow you to alter existing node classes.
- (Think about the BST, and so something in each node without modify node. Orignally add export method and call in each node, but cannot add the export method)
<hr>
- Besides, he questioned whether it makes sense to have the XML export code within the node classes. 
- The primary job of these classes was to work with geodata. 
- And plus, it was highly likely that after this feature was implemented, someone from the marketing department would ask you to provide the ability to export into different foramt, or request some other weired stuff. This would force you to change those precious and fragile classes again.
<hr>
In short, unrelated method should not be included node structure. When it is allowed to add addtional method to nodes, then other unrelated method could be added to. 

# Solution
The Visitor pattern suggests that you place the new behavior into a separate class called visitor, instead of trying to integrate it into existing classes. The original object that had to perform the behavior is now passed to one of the visitor's methods as an argument, providing the method access to all necessary data contained within the object. 



