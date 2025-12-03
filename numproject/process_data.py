import numpy as np


ids, xyz,nft,bmn= np.genfromtxt('numproject/RealEstate-USA.csv', delimiter=',', usecols=(0,2,3,4), unpack=True, dtype=None,skip_header=1)

print(ids)
print(xyz)
print(nft)
print(bmn)
print("th mean of the data is: " , np.mean(ids))
print("the average is",np.average(ids))
#different math operations
print("the square if the xyz is",np.square(xyz))


addition=ids+xyz
print("the addition is",addition)
#starsc perations
print("the percentaile of the data is",np.percentile(xyz,25))

print("the min of the data is",min(nft))
#trignometric operations
var=(xyz/np.pi)+1
sine=np.sin(var)
cose=np.cos(var)
tagen=np.tan(var)
print("the sine function on the data is",sine)
print("the cose function on the data is",cose)
print("teh tagent on the data is ",tagen)
#calculation on logirithm
rao=np.log(var)
rao2=np.log10(var)
print("the log of the data is",rao)
print("the log of the data is",rao2)
#sin hyperbolic values
sinh_value=np.sinh(var)
print("the sign hyperboloc value of real sratae data is",sinh_value)
cosh_value=np.cosh(var)
print("the cos h value is",cosh_value)
tanh_value=np.tanh(var)
print("the value of tanhvalue is",tanh_value)
d2xyzids=np.array([xyz,ids])
print("the two diementail array is ",d2xyzids)
print("the sixe of two dimential array is",d2xyzids.size)
print("the shape of two diemential array is",d2xyzids.shape)
print("the size of coloumn 1 is",xyz.size)

arr=np.array([[1,2,3],[6,383,49]])
print("the size of array is ",arr.size)
print("array shape  is",arr.shape)
print("the type of array is",arr.ndim)
darray2=np.array([ids,xyz])
print("the type of array is",darray2.ndim)
print("the size of array is",darray2.size)
print("the shaape of the array is",darray2.shape)
print("the type of array is",darray2.dtype)

for elem in np.nditer(darray2):
  print(elem)
  
  
for index,elem in np.ndenumerate(darray2):
  print(index,elem)  

