a = [(x,y) for x in range(1,5) for y in range(6,10)]
print(a)
print(len(a))

ll = []
for x in range(1,5):
    for y in range(6,10):
        ll.append((x,y))
print(ll)