# 装饰器
def simple_decorator(f):
    def wrapper():
        print("func enter")
        f()
        print("func exit")
    return wrapper

@simple_decorator
def hello():
    print("Hello World!")
    
hello()