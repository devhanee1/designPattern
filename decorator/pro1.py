
def display(func):
    print("------")
    func()
    print("------")

def display2(func):
    def wrapper():
        print("=====")
        func()
        print("=====")
    return wrapper

@display2
def hello():
    print("Hello") 

'''
display(hello)
t = display2(hello)
t()
'''

hello()