d1 = {'a':1,'b':2,'c':3}

print(d1.keys())
print(d1.values())
print(d1.items())

swap = {}
for x,y in d1.items():
    print(x,' ',y)
    swap[y] = x

print(swap)
print(swap.pop(2))
print(swap)
 
