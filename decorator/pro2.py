def func1(*arg):
    print("func1")
    print(type(arg))
    print(arg)

def func2(**kwargs):
    print("func2")
    print(type(kwargs))
    print(kwargs)

def func3(*args, **kwargs):
    print("func3")
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)


func1(1,2,3)
func2(a=1, b=2, c="hello")
func3(1,2,3, a=1, b=2, c="Lion")