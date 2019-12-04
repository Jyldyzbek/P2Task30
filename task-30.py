a = input('Vedite svoyu skazku: ').split()
b = []
for s in a:
    if s not in b:
        print(s, a.count(s))
    b.append(s)