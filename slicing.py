listmu = [10, 20, 30, 40, 50, 60]
listku = []

for i in range(2, 5):
    listku.append(listmu[i])

print(f'listku={listku}')

#pythonic
listkita = listmu[2:5]
print(f'listkita={listkita}')

kata = 'PEMBELAJARAN'
print(kata[3:10])