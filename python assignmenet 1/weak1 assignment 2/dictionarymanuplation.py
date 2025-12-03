# 1.  Check if a value exists in a dictionary 
# 2.  Get the key of a minimum value from the following dictionary 
# 3.  Delete a list of keys from a dictionary 


# 1.  Check if a value exists in a dictionary 
record={
'name':'rao',
'class':'bscs',
'roll number':120,
'section':'B'
}

records={}
n=input('enter the dictionary you want to search')
if n in record.values():
    print("found ")
else:
    print("not found")    

# 2.  Get the key of a minimum value from the following dictionary 

value={
'Abdullah':120,
'Ali':121,
'sameed':121,
'Aabdullah khan':115
}

minimum=min(value,key=value.get)
print(" the minimum value is",minimum)

# 3.  Delete a list of keys from a dictionary 
keys={
'Abdullah':120,
'Ali':121,
'sameed':121,
'Aabdullah khan':115
}

keys_to_delete={'Abdullah','Ali'}
for key in keys_to_delete:
    keys.pop(key, None)  
print(keys)   
