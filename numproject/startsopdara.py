import numpy as np


npn, xyz,nft,bmn= np.genfromtxt('numproject/startsup_2021end.csv', delimiter=',', usecols=(0,2,3,5), unpack=True, dtype=('int32','U100','U100','U100'),skip_header=1)

print(npn)
print(xyz)
print(nft)
print(bmn)
print("the size of array is",npn.size)
#we are converting dollar sign with float because dollar sign makes our data in string form so 1 we
# have to convert our data in float value so that we can easily apply different operations in it

col_index = 2
xyz = np.char.replace(xyz, '$', '')
xyz =  xyz.astype(float)
print(xyz)
print(type(npn))

#arithmatic operattion
addition=xyz+npn
subtraction=npn-xyz
multipliction=npn*xyz
division=npn/xyz
print("the addition is",addition)
print("the multiplication is",multipliction)
print("the division is ",division)
print("the subtraction  is",subtraction)
#static operations on data 
print("startsup data npn mean",np.mean(npn))
print("startsup data npn average is",np.average(npn))
print("startsup data npn std is",np.std(npn))
print("startsup data npn meadian is",np.median(npn))
print("startsup data npn mean",np.min(npn))
print("the maximum is ",np.max(npn))

# different operations on data 
print("the square is ",np.square(npn))
print("the square root is",np.sqrt(xyz))
print("the power of non is",np.power(xyz,npn))
print("the abs is",np.abs(npn))

#different trignometric operations
npn=(npn/np.pi)+1
#calculateing the different operations
sinevalue=np.sin(npn)
cosevalue=np.cos(xyz)
tagentvalue=np.tan(npn)
print("Sine values:", sinevalue)
print("Cosine values:", cosevalue)
print("tagent values:", tagentvalue)

# Calculate the natural logarithm and base-10 logarithm
logarray=np.log(npn)
logarray_10=np.log10(xyz)
print('the value of log is ',np.log(npn))
print("the log with base 10 is ",np.log10(xyz))
#hyperbolic values
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(npn)
print("the  Tangent values:", tanh_values)
#Example: Inverse Hyperbolic Sine
# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(xyz)
print("Inverse Hyperbolic Sine values:", asinh_values)
#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(xyz)
print(" Cosine values:", acosh_values)
#2 dimential array
darray2=np.array([npn,xyz
          ])
print("The wo gimential array is",darray2)
print("the diementions of array is ",darray2.ndim)
print("the sixe of array is",darray2.size)
print("the shaoe of the array is",darray2.shape)
print("the type of array is",darray2.dtype)

#slicing in array
slicingarray=xyz[0:2:8]
print("slicing in array is",slicingarray)

d2reshapearray=np.reshape(darray2,(1,1872))
print("reshape of the array is ",d2reshapearray)
print("the shape of the array is",d2reshapearray.ndim)
print("te shae of the array is ",d2reshapearray.shape)
#loop opeartion on data 
for elem in np.nditer (darray2):
    print(elem)
#loop with elements indexing
for index,elem in np.ndenumerate(darray2):
 print(index,elem)


print()