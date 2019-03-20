n = [int(i) for i in input().split()]
s = []
for i in n:
    if n.count(i)>1:
        s.append(i)
print(set(s))
