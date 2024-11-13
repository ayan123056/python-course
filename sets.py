set1 = {1,1,3,3,7,7}
print(set1)
set2 = {4,5,7,7}
print(set2)
set2.add(100)
print(set2)
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.symmetric_difference(set2))