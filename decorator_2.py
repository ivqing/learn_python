import functools

# decorator suports @log & @ log('execute')
def log(func, text=None):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s %s():' % (text, func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def hit():
    pass

hit()

print('_______________________________')

#@log('execute')
def hi():
    pass

hi()
