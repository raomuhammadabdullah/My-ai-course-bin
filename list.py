a=[10,"rao",30,70,85,90]
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(type(a[4]))
print(type(a[5]))

print("next run")

a=[12,"rao",60,83,84,84]
b=[38,"hsj",82,83,92]
print(a)
print(b)


a=[]
a.append(10)
print("after apend",a)
print("next run")

a.insert(0,5)
print("next run")

a.extend([10,3,6,])
print("after extend",a)


b=[]
print(b)
print("next run")

a=[10,83,48,93]
a[2]=25
print(a)

a.remove(93)
print("after remove",a)
pop_valed=a.pop(2)
print(a)

del a[0]
print(a)


v=[
[10,50.30],
[30,48,58],
[39,74,28]
]
print(v[0][1])
