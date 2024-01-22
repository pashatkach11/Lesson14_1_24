spisok = [12, 3, 4, 10, 8]

if len(spisok) != 0 and len(spisok) != 1:
    spisok.insert(0, spisok[-1])
    spisok.pop(-1)

print(spisok)