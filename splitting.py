teks = 'belajar python dasar'
listku = []
kata = ''
for huruf in teks:
    if huruf != ' ':
        kata += huruf
    else:
        listku.append(kata)
        kata = ''
listku.append(kata)
print(f'teks: {teks}')
print(f'listku: {listku}')

#pythonic:
listmu = teks.split()
print(f'listmu: {listmu}')