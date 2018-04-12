best = {'b', 'e', 's', 't'}
rest = {'r', 'e', 's', 't'}
pest = {'p', 'e', 's', 't'}

print(best | rest | pest)
print(best & pest & rest)
print(best - pest - rest)
print(best ^ pest)