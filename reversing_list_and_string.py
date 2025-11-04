listku = [10, 20, 30, 40, 50, 60]
listmu = []

for i in range(len(listku)):
    reverse_i = len(listku) - 1 - i
    listmu.append(listku[reverse_i])

print(f'listku={listku}')
print(f'listmu={listmu}')

#pythonic:

listkita = listku[::-1]
print(f'listkita={listkita}')

kata = 'BELAJAR'
kata_reverse = kata[::-1]
print(kata_reverse)