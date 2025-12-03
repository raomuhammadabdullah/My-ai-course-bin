import numpy as np


npn, xyz,nft,bmn= np.genfromtxt('numproject/RealEstate-USA.csv', delimiter=',', usecols=(0,2,3,5), unpack=True, dtype=('int32','int64','int32','f8'),skip_header=1)

print(npn)
print(xyz)
print(nft)
print(bmn)
print("data type od npn is",npn.dtype)
print("data type od npn is",xyz.dtype)
print("data type od npn is",nft.dtype)
print("data type od npn is",bmn.dtype)
# stats opeation
print("the mean of the data is",np.mean(xyz))
print("the average of the data is ",np.average(xyz))
print("the average of the value is ",np.average(xyz))
print("the median of the function is",np.median)
print("the minimum value is",np.min(xyz))
print("the maximum value is",np.max(xyz))
#math operations on data 
print("the square of the data is",np.square(xyz))
print("the sqrt of the data is",np.sqrt(xyz))
print("the power of the values are",np.power(xyz,npn))
print("the abs of the value is ",np.abs(xyz))

addition=xyz+npn
subtraction=xyz-npn
multiplication=xyz*npn
division=xyz/npn
print("the additionn of the data is ",addition)
print("the subtraction of the data is ",subtraction)
print("the multiplicaton of the data is ",multiplication)
print("the division of the data is ",division)


npnpy=(xyz/np.pi)+1
sine_values = np.sin(npnpy)
cosine_values = np.cos(npnpy)
tangent_values = np.tan(npnpy)
print("the in of the value is",sine_values)
print("the coe value is",cosine_values)
print("the tagent of the value is",tangent_values)

#2 diemention array
d2array=np.array([npn,xyz])
print("the size of 2d array is ",d2array.size)
print("the shape of the array  is ",d2array.shape)
print("the length of array is ",d2array.ndim)
print("the data types of array is",d2array.dtype)

#loop operaion in numpy
for elem in np.nditer(xyz):
 print(elem)
for index,elem in np.ndenumerate(xyz):
 print(index,elem)


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(xyz)
log10_array = np.log10(npn)

print("Zameen.com Price - div - pie  - Natural logarithm values:", log_array)
print("Zameen.com Price - div - pie  = Base-10 logarithm values:", log10_array)

d2long=np.reshape(d2array,(1,400))
print("2 dimentional arrary - np.reshape ", d2long)
print("2 dimentional arrary - np.reshape " , d2long.size)
print("2 dimentional arrary - np.reshape ndim " , d2long.ndim)
print("2 dimentional arrary - np.reshape shape " , d2long.shape)
print("2 dimentional arrary - np.reshape  " , d2long.ndim)




