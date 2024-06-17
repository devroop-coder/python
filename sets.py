# Repeatations not allowed

s1 = { 54, 55, 56, 57, 58, 59, 60}
s2 = { 55, 56, 57, 58,59}

emptySet = ()

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1 - s2
print(s1.isdisjoint(s2))

s2.add(60)
print(s2)
s2.remove(60)
s2.discard(70)
s1.pop()
print(s1)
print(s2)
s1.update(s2)
print(s1)
s1.clear()
print(s1)
del s1
