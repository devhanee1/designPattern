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


