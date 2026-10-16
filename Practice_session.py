import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)
print(a.size)
print(a.ndim)
print(a.transpose())
print(a.dtype)
print(a.itemsize)

print("MEthod ")
print("==============")
a.resize([4,4],refcheck=False)
print(a)
b=a.flatten()
print(b)
# sum


import numpy as np
from scipy import stats
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.sum())
print(np.mean(a))
print(stats.mode(a))
print(np.median(a))

# standard derivation 

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(np.std(a))
print(a.min())
print(a.max())
print(np.zeros([4,4]))


# array creations method 

import numpy as np
a=np.arange(10,100,10)
print(a)
b=np.arange(200,10,-10)
print(b)
c=np.linspace(9,100,7)
print(c)
# random 
d=np.random.randint(1,9,4)
print(d)

# ones , full
import numpy as np
a=np.ones([5,4])
print(a)

b=np.full([5,5],10)
print(b)


#  type and type conversion , can_cast
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.dtype.type)
b=a.astype(float)
print(b.dtype)
c=np.can_cast(a,str)
print(c)

print(a[1:2,2])
print(a[1,3])


# Boolean indexing and logical operators 

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a[(a>4) & (a>6)])

c=np.logical_and(a>4,a<7)
print(a[c])

d=np.logical_not(a>4,a<7)
print(a[d])

e=np.logical_or(a>4,a<7)
print(a[d])

f=np.any(a>10)
print(a[f])

o=np.any(a>7)
print(a[o])
