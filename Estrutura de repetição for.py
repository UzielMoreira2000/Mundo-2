'''
for a in range(0, 6):
    print(a)
print('\n')

for b in range(6, 0,-1): # decrementa de um em um
    print(b)
print('\n')

for c in range(0, 6, 2): # conta de dois em dois, o ultimo numero determina
    print(c)

n = int(input('digite um numero:')) # printa o range ate o valor escolhido
for d in range(0, n+1):
    print(d)
print('\n')

i = int(input('inicio da contagem:'))
f = int(input('fim da contagem:'))
p = int(input('passo da contagem:'))

for c in range(i, f+1, -p): # usar o passo negativo para contagem regressiva
    print(c)
'''

s = 0
for a in range(0, 4):
    n = int(input('digite um valor:'))
    s = s + n   # pode ser escrito como: s += n
print('\no somatorio dos valores é {}'.format(s))
