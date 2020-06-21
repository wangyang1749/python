# usage *args **args
def function(*args):
    print(args, type(args))
function(1) # (1,) <class 'tuple'>

def function(x, y, *args):
    print(x, y, args)
function(1, 2, 3, 4, 5) # 1 2 (3, 4, 5)

def function(**kwargs):
    print( kwargs, type(kwargs)) # {'a': 2} <class 'dict'>
function(a=2)

def function(**kwargs):
    print(kwargs)
function(a=1, b=2, c=3) #{'a': 1, 'b': 2, 'c': 3}

def function(arg,*args,**kwargs):
    print(arg,args,kwargs)
function(6,7,8,9,a=1, b=2, c=3) # 6 (7, 8, 9) {'a': 1, 'b': 2, 'c': 3}

