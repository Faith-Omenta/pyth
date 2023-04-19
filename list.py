# .append adds an element at the end of a list
grocery=["broccoli","cucumber","tomato","eggplant"]
newgrocery=["onion","banana","orange"]

grocery.append(newgrocery)
print(grocery)

grocery.append("mangoes")
print(grocery)
print(type(grocery))

stock=["eggs","cookies","bread"]
newstock=["salt","flour","kales"]
stock.extend(newstock)
print(stock)

# concatinate two lists in the following
list1=["hello "," take"]
list2 =[" dear "," sir "]
list4=[x + y  for x in list1 for y in list2]
print(list4)

# list1.extend(list2)
# print(list1)

# write a programm to find value of 20 in the list and if it is present replace it with 200
# list3=[5,10,15,20,25,50,20]
list3=[5,10,15,20,25,50,20]
x=list3.index(20)
list3[x]=200
print(list3)

# write a program to remove all occurrence of item 20
# list3=[5,10,15,20,25,50,20]
list4=[5,10,15,20,25,50,20]
while 20 in list4:
    list4.remove(20)
print(list4)
