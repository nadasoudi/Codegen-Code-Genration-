>>> import numpy as np
>>> a = np.array(['a', 'b', 'c', 'd'])
>>> a
array([ 'a', 'b', 'c', 'd'])
>>> a.dtype
dtype('<U3')
>>> a.size
3
>>> a.itemsize
3
>>> a.shape
(3,)
>>> a.strides
(3,)
>>> a.strides[0]
3
>>> a.strides[1]