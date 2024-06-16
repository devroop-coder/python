l= [5,6,8,2,7,6,21,5,54,6,54,32,5,6,54,5,9]
print(l)
print(l.index(54)) #gives index of the element

l.append(555) #add elementi list last position
print(l)
print(l[5:10])

l.sort()
print(l)
l.sort(reverse=True)
print(l)

l.reverse()
print(l)

l.insert(5,88)
#    index  element

print(l.count(54))

m= l # refers to the list

n = l.copy() #make a copy of the list

n[0]=88 #replace value at a given index

print(n)

o =[55,85,8565,65,65,85,5]

m.extend(o)  # join two lists together

print(m)

k = l+m # make a new list by joining lists together

print (k)

