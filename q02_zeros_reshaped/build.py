# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
zeros_array_reshaped = np.reshape(zeros_array, (2,3,4))
zeros_array_reshaped
