# New Paper / Subscribe / Observer / ...

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
