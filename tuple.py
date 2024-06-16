tup = (88,65,6,85,2,69,5,6,5,96)
print(tup.count(5)) 
print(tup.index(5))
print(tup.index(5,7,9)) # ele ,1st ind , last ind

list = list(tup)

list.append(111)
list.insert(5,555)
list.sort()
tup = tuple(list)
print(tup)
print(tup.count(5))

oneEleTup =(1,)