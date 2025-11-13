a=[10,20,30,40,'age']
print(type(a))
print(a[0])
print(a[2])
print(type(a[4]))
a.append(20)
print(a)
a.extend([50,40])
print(a)
a.insert(100,50)
print(a)
a.remove('age')
print(a)
b=a.pop(0)
print('deleted elemen is',b)
a.clear()
print(a)

c=[
 [10,20,30],
[ 30,40,50],
[60,70,80]
]
print(c[0][2])
