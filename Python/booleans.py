#Booleans can evaluate is somethong is True or False

print(9 > 10) #False
print(5 < 8) #True
print(8 == 8) #True

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))
