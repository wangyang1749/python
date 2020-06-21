import  time
def decorator(func):# 这里需要了解如何将函数做为一阶参数
    """
    这是个计时装饰器
    """
    def wrapper(*args,**kwargs): #这里需要了解可变参数
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time-start_time)
    return wrapper

# 这里相当于把整个say_hello的内存地址当做参数传给了decorator(),在wrapper方法中的func()方法等于在调用say_hello()
@decorator 
def say_hello():
    time.sleep(1)
    print("say_hello!")

#只需要在函数的定义前加上@和装饰器的名称
@decorator
def say_goodbye():
    time.sleep(1)
    print("say_goodbye!")


if __name__ == '__main__':
    say_hello()
    say_goodbye()
