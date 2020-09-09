import numpy as np
### Create a 3x1 numpy array
a = np.array([1,2,3])

### Print object type
print(type(a))

### Print shape
print(a.shape)

### Print some values in a
print(a[0], a[1], a[2])

### Create a 2x2 numpy array
b = np.array([[1,2],[3,4]])

### Print shape
print(b.shape)

## Print some values in b
print(b[0,0], b[0,1], b[1,1])

### Create a 3x2 numpy array
c = np.array([[1,2],[3,4],[5,6]])

### Print shape
print(c.shape)

### Print some values in c
print(c[0,1], c[1,0], c[2,0], c[2,1])