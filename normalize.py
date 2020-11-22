import numpy as np
np.random.seed(21)

# Code starts here

# create random 5x5 array

z = np.random.random((5,5))

# minimum and maximum values

zmax = z.max()
zmin = z.min()

# normalize

range = zmax - zmin
z_norm_1 = z - zmin
z_norm = z_norm_1 / range

# display
print(zmax)
print(zmin)
print(z_norm)
