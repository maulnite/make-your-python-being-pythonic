a = 10
b = 20
print('before switch: ')
print(f'a = {a}, b = {b}')

c = a
a = b
b = c
print('after switch: ')
print(f'a = {a}, b = {b}\n')

# its same like:

a, b, c = 10, 20, 30
print('before switch: ')
print(f'a = {a}, b = {b}, c = {c}')

a, b, c = c, b, a
print('after switch: ')
print(f'a = {a}, b = {b}, c = {c}\n')

a, b, c = 10
print(f'a = {a}, b = {b}, c = {c}\n')