def lipat_ganda(x):
    return x * 2

listku = [10, 20, 30]
listmu = []

for item in listku:
    listmu.append(lipat_ganda(item))

print(f'listku={listku}')
print(f'listmu={listmu}')

#pythonic:
listkita = list(map(lipat_ganda, listku))
print(f'listku={listku}')
print(f'listkita={listkita}')