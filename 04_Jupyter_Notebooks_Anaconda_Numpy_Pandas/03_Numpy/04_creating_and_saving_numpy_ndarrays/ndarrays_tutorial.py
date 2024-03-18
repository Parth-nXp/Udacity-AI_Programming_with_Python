# We import NumPy into Python
import numpy as np  

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Let's print the ndarray we just created using the print() command
print('x = ', x)

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World'])

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# We create a rank 1 ndarray that contains integers
x = np.array([1,2,3])

# We create a rank 1 ndarray that contains floats
y = np.array([1.0,2.0,3.0])

# We create a rank 1 ndarray that contains integers and floats
z = np.array([1, 2.5, 4])

# We print the dtype of each ndarray
print('The elements in x are of type:', x.dtype)
print('The elements in y are of type:', y.dtype)
print('The elements in z are of type:', z.dtype)

# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# We print x
print()
print('x = ', x)
print()

# We print the dtype x
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as 
np.save('my_array', x)

# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

# We print y
print()
print('y = ', y)
print()

# We print information about the ndarray we loaded
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)