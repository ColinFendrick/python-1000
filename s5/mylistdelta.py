zlist = ["Fred", "Ralph", "Zelda", "Zoe"]

print(type(zlist))
for index in range(len(zlist)):
    zlist[index] = "Guest " + zlist[index]
    print(zlist)
