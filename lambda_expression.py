def lipat_ganda(x):
    return x * 2

listku = [10, 20, 30]
listmu = list(map(lipat_ganda, listku))
print(f'listku={listku}')
print(f'listmu={listmu}\n')

#pythonic
listkita = list(map(lambda x: x*2, listku)) #lambda [param]: [return] --> anonymous function
print(f'listku={listku}')
print(f'listkita={listkita}')