l1 = ['1','2','3']
l2 = ['a','b','c','d']
l1.append('4')
print(l1)

x1 = ":".join(l1)
print(x1)

for a,b in zip(l1,l2):
    print(a,b)