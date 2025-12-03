# String Manipulation 
# 1. Write a program to create a new string made of an input string’s first, o
# middle, and last character. 
n=(input("enter yur string"))
middle=len(n)//2
result=n[0]+n[middle]+n[-1]
print(result)

# 2. Write a program to count occurrences of all characters within a string 
count={}
n='welcome to home'
for i in n:
    if i in count:
        count[i]=+1
    else:
        count[i]=1
print(count)



# Given. 
# 3. Reverse a given string 
# 4. Split a string on hyphens 
# 5. Remove special symbols / punctuation from a string 

t='intoduction_to_%$_class'
print(t[::-1])
word=t.split()
print(word)
        
t = 'intoduction_to_%$_class'
clean = ""

for ch in t:
    if ch.isalnum():   
        clean += ch




  