import numpy as np


ids, xyz,nft,bmn= np.genfromtxt('numproject/fastfoodresturant.csv', delimiter=',', invalid_raise=False, usecols=(0,1,2,3), unpack=True, dtype=('U100','U100','U100','U100'),skip_header=1)

print("the ids are",ids)
print(xyz)
print(nft)
print(bmn)


#arithmatic operations
addition=ids+xyz
subtraction=ids+bmn
print("the additon is ",addition)
print("the subtraction is",subtraction)
#2d array
darray2=np.array([ids,xyz])
print("the shape of the array is ",darray2.ndim)
print("the datatype of the arrays id",darray2.dtype)
print("the size of the array is",darray2.size)

#reshapping of array is 
reshappingarray=np.reshape(darray2,(1,19980))
print("the shape of the array is ",reshappingarray.ndim)
print("the size of the array is",darray2.size)





