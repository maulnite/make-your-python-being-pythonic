nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']

for i in range(len(nim)):
    print(f'{nim[i]}--{nama[i]}')

#pythonic:

for i, data_nim in enumerate(nim): #enumerate akan mengembalikan pasangan index dan data
    print(f'{data_nim}--{nama[i]}')