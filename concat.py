listku = ['belajar', 'python', 'dasar']
kalimat = ''
for kata in listku:
    kalimat += kata + ' '
print(f'listku: {listku}')
print(f'kalimat: {kalimat}')

#pythonic:
kalimat2 = ' '.join(listku)
print(f'kalimat2: {kalimat2}')
