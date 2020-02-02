def not_very_simply_decorator(enter_msg,exit_msg):
    def simple_decorator(f):
        def wrapper():
            print(enter_msg)
            f()
            print(exit_msg)
        return wrapper
    return simple_decorator

@not_very_simply_decorator("func enter","func exit")
def hello():
    print("Hello World")

hello()