ss = 0
zlist = {1: "Mr. Ed", "alive": "Miss Daisy", 3: "Mr. T", 4: "Dr. Who"}
for entry in zlist:
    ss += 1
    print(ss, ".)", zlist[entry], entry.__hash__())