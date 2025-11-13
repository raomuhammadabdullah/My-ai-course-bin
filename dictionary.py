rao={
'name':'ali',
'class':'bscs',
 'roll':'121'
}
print(rao['name'])

rao['ali']=('name')
print(rao)


del(rao)['class']
print(rao)


rao.clear()
print(rao)




country_capital={
'italy':'rome',
'pak':'islamabad'
} 

for country in country_capital:
   print(country)
for country in country_capital:
    capital = country_capital[country]
    print(capital)

print(len(country_capital))
