import china
from china import cook as china_cook
from japan import cook as japan_cook
from japan import is_prime
try:
    from brazil import cook
except ImportError:
    print("Brazil not found")

from latam.peru import cook as peru_cook # this is a package
from latam.mexico.jalisco import cook as jalisco_cook
from latam.mexico.mexico import cook as mexico_cook

#import sys
#import pandas

def cook():
    print("We are spanish making paella")


#the last function with the name will take that definition (only risk of from ... import ... command) to avoid

#print("Hello World")
print(china.greet)
#china.cook()
#for p in sys.path:
    #print(p)

cook()
china_cook()
japan_cook()


print(f"1027 is prime {is_prime(1027)}")
peru_cook()
jalisco_cook()
mexico_cook