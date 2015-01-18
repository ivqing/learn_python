import functools

# decorator, print the log of func
def log(func):
    @functools.wraps(func) # decorator handling signature problem
    def wrapper(*args, **kw):
        print('begin call %s' % func.__name__)
        return func(*args, **kw)
        print('end call %s' % func.__name__) # this will not excute
    return wrapper

@log
def nothing():
   print('hello decorator') 

nothing()
