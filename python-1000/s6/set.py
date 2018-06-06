cat = {'c', 'a', 't'}
car = set()
car.add('c')
car.add('a')
car.add('r')

print (cat)

# duplicates excluded
prefix = {'Pig', 'Cat', 'Pig', 'CAT', 'Dog'}
for dat in prefix:
    print(dat)

prefix2 = set(('pig', 'Mouse', 'Pig', 'Dog'))

#intersections
print(prefix2.intersection(prefix))

#union
print(prefix2.union(prefix))

print(type({}))
print(type({"Ed", "Dan"}))
print(type({1: "Mr Ed", 2: "Mr Dan"}))