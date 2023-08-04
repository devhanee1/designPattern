# Usage
- Newspaper
- Subscribe
- Observer
- Graphical User Interface
-  Custom Button class, and you want to let the clients hook some custom code to your button so that it fires whenever a user press a butonZ

# Intent
Observer is behavior design pattern that lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they're observing. 

# Problem
Imagine that you have two types of objects: a Customer and a Store. 
The customer is very interested in a particular brand of product which should become available in the store very soon. 

The customer could visit the store every day and check product availability. But while the product is still
en route, most of these trips would be pointless.

On the other hand, the store could send tons of emails (which might be considered spam) to all customers
each time a new product becomes available. This would save some customers from endless
trips to the store. At the same time, it'd upset other customers who aren't interested in new products.

It looks like we've got a conflict. Either the customer wastes time checking product availability or the
sotre wastes resources notifying the wrong customers.

![image](https://github.com/devhanee1/designPattern/assets/37257706/bb8e8275-c112-45c0-9685-e5fbe8e51ada)

# Solution

![image](https://github.com/devhanee1/designPattern/assets/37257706/722fe815-4332-472f-a354-6d87c7ab50ba)
![image](https://github.com/devhanee1/designPattern/assets/37257706/d1594aae-e009-4be7-9ab5-91d278033f31)

It's crucial that all subscribers implement the same interface and that the publisher communicates with them
only via that interface. This interface should declare the notification method along with a set of parameters that
the publisher can use to pass some contextual data along with the notification. 

# Real-World Analogy
If you subscribe to a newspaper or magazine, you no longer need to go to the store to check if the next issue is available. 
Instead, the publisher sends new issues directly to your mailbox right after publication or even in advance.

The publisher maintains a list of subscribers and knows which magazines they’re interested in. 
Subscribers can leave the list at any time when they wish to stop the publisher sending new magazine issues to them.


Adding new subscribers to the program doesn’t require changes to existing publisher classes, 
as long as they work with all subscribers through the same interface.


# Structure
![image](https://github.com/devhanee1/designPattern/assets/37257706/b3e96aa1-851a-4055-9512-6bed4e0553ba)



