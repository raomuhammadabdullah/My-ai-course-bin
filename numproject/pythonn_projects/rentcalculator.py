#input total number of persons 
#input the amout that is spend on food
#input charge per unit
#electricity unit spend

rent=int(input("enter the total rent = "))
food=int(input("enter amount that is spend on food = "))
electricity_spend=int(input("enter the total of electricity that is spend ="))
charge_per_unit=int(input("enter the charge per unit = "))
person=int(input("enter the total number  of person tha is living = "))
electricty=electricity_spend*charge_per_unit
total=(food+rent+electricty)//person
print("the amount thay you have to give = ",total)



