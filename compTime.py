import time

def compTime(func):

    def decorator(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()

        print ("Time:", te - ts, end=" ")
        
        return result

    return decorator