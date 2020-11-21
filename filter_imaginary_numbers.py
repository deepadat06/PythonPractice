# Code starts here
import numpy as np
# initialize array

array = np.array([3,4.5,3+5j,0])

# boolean filter

real = np.isreal(array)
real_array = array[real]

# boolean filter

imag = np.iscomplex(array)
imag_array = array[imag]

# Code ends here
