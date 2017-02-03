#! Insret the current directory part to Python Part
import sys
import os
cwd = os.getcwd() # Current Working Directory

sys.path.append(cwd)
#print(sys.part)

# Test the module: generate_list
from generate_list import printIt
for x in range(1, 1000):
    printIt()