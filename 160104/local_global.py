
def use_local():
    x = 33
    print "Local variable x is", x

def use_global():
    print "Global variable x is", x

x = 100
use_local()
use_global()
