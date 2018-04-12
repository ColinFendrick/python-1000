cat = {'c', 'a', 't'}
car = set()
car.add('c')
car.add('a')
car.add('r')

print(cat, car)
print("cat | car === union", cat | car)
print("cat & car === intersect", cat & car)
print("cat - car === rmeove common car from cat", cat - car)
print("cat ^ car === order dif", cat ^ car)

