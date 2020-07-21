  
# Python script to sort an array according to given index. Helpful to de-obfuscate strings in macros.

# Import Stuff 
import numpy as np
from array import *
import array as ar

# Set the strings as elements array
array_var = np.array([<ARRAY GOES HERE>])

# Insert the index[] 
idx = [<INDEX GOES HERE>]

# Reorder the array values using indices
list1 = array_var[idx]

#Join the elements and store as string
print("".join(list1))
