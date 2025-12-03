# List Manipulation 
# 1.  Reverse a list in Python 
# 2.  Turn every item of a list into its square 
# 3.  Remove empty strings from the list of strings 
# 4. Add new item to list after a specified item 
# 5.  Replace list’s item with new value if found 

# 1.  Reverse a list in Python 
n=[1,3,5,6,7,8]
print(n[::-1])
t=[]
# 2.  Turn every item of a list into its square 
for i in n:
 t.append(i*i)
print(t)
# 3.  Remove empty strings from the list of strings
x=[1,2,3,4," ",3," ",3,4,3,2]
y=[]
for item in x:
 if item!=" ":
  y.append(item)
print(y)  
 # 4. Add new item to list after a specified item
fruits = ["apple", "banana", "cherry", "date"]
index = fruits.index("banana")
fruits.insert(index + 1, "mango")
print(fruits)
# 5.  Replace list’s item with new value if found
fruits = ["apple", "banana", "cherry", "date"]

if "banana" in fruits:      # check if item exists
    index = fruits.index("banana")
    fruits[index] = "mango"

print(fruits)






