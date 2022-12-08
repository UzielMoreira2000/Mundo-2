
#comparação entre FOR  e WHILE
'''
for c in range(0,9):
    print(c,end=' ')
print('fim')

c=0
while c < 10:
    print(c,end=' ')
    c += 1
print('fim')


r = 'S'       # recebe valores enqunto o usuario confirmar com S ou N
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('fim')
'''

pares = 0
impares = 0
n = 1

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print('{} valores eram pares, {} impares'.format(pares,impares))
print('fim')





