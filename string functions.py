a="raoabdullah"
print(a[1:4])#slicing function
print(a[-3:-1])
# string functions
a="i am apitalize function"
print(a.replace("a","b"))#replace function
print(a.find("l"))#find function
print(a.count("abdullah"))#count functionabdullah"
print(a.endswith("lah"))#ends with function
print(a.capitalize())#count function

name=input("enter your name")
b=print(name)
print(len(name))
name="hi i am 4$"
print(name.count("$"))
a=int(input("enter your 1 number"))
b=int(input("enter your 2 number"))
c=int(input("enter your 3 number"))
if a>b and a>c:
    print("1 number is greate")
elif b>a and b>c:
    print("2 number is greater")
else:
    print("3 number is grater")

    marks=int(input("enter your marks"))
    if marks>=90:
        print("you have secure grade A")
    elif marks>=80 and marks<90:
        print("you have secure grade B")
    elif marks<80 and marks==70:
        print("you have secure c grade")
    else:
        print("you have secure d")  

    #program to check if a number is a multiple of 7 or not
a= int(input("enter a number"))
if a%7==0:
  print("number is multiple of 7")
else:
    print("number is not multiple of 7")
num=int(input("enter your age"))
if num>=18:
    print("you are eligible for driving")
else:
    print("you are not eligible for driving")    