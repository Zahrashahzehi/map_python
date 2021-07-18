numbers = [1,2,3,4,5]
doublse = list(map(lambda num : num *2 , numbers))
print(doublse)
print(doublse)
print("==========================")
names = ["zahra" , "atta" , "sara"]
upper_name = list(map(lambda name : name.upper() , names))
print(upper_name)
print("======================================")
pepale = [{"name" : "zahra" , "family" : "shahzehi" , "age" : 20} ,
{"name":"atta" , "family": "attarian" , "age" : 21}]
family = list(map(lambda person : person["family"] , pepale))
print(family)