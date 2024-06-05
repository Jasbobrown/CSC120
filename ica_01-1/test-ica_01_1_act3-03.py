#! /usr/bin/python3

from ica_01_1_act3 import *



print("This print was done by the testcase, before the function was called.")
retval = str_mult("",1000*1000)
print("This print was done by the testcase, after the function was called.")
print()

print(f"The function returned: {repr(retval)}")

