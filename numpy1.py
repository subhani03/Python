""" import numpy 
a=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print(a[1])
print(a[1]+a[2]) 
print(a[1:5])
print(a[5:4])
print(a[:4])
print(a[4:])
print(a[-3:-1])
print(a[1:10:2])
print(type(a))
print(numpy.__version__) """
#two dimension
""" import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0,1])
print(a[1,1:4])
print(a[0:1,2])
print(a[0:1,1:4])
print(a[0:1]) """
#multi dimension
import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a[0,1])
print(a[1,1])
b=np.array(4)
c=np.array([1,2,3])
print(a.ndim)
print(b.ndim)
print(c.ndim)


