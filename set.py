x=set()
print(type(x))
n=set([1,2,3,4,5,6,7,7,8])
print(type(n))
print(n)

t={1,2,3,4,'rao','rajpoot'}
print(type(t))
print(t)

empty_dictionart={}
print("the type of empty dictionary is",type(empty_dictionart))


emty_set=set()
print(type(emty_set))



# using add() method





companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)