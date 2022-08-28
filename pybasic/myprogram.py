#   1---
#import mymodule
#mymodule.func_in_module()

#  2----

#import mymodule as mm
#mm.func_in_module()

#   3----

#from mymodule import func_in_module
#func_in_module()

#    4------

from mymodule import *
func_in_module()