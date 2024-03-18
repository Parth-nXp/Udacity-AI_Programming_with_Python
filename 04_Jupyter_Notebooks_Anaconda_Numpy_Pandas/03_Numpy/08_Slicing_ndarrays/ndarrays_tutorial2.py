import numpy as np
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 4th columns
Z = X[1:4,2:5]

# We print Z
print()
print('Z = \n', Z)
print()


# We change the last element in Z to 555
Z[2,2] = 555

# We print X
print()
print('X = \n', X)
print()