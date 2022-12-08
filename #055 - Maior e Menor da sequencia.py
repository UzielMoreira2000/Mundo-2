
'''
Exercício Python 055: Faça um programa que leia o peso
 de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

maiorpeso = 0
menorpeso = 0

for a in range(1,5):
    peso = float(input('{}°PESSOA - Digite peso: '.format(a)))
    #identifica maior peso
    if a == 1:
        maiorpeso = peso
    if peso > maiorpeso:
       maiorpeso  = peso
    # identifica menor peso
    if a == 1:
        menorpeso = peso
    if peso < menorpeso:
       menorpeso  = peso

print('O maior peso é {}Kg'.format(maiorpeso))
print('O menor peso é {}Kg'.format(menorpeso))
'''
pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)

print('O maior peso é {}Kg' .format(max(pesos)))
print('O menor peso é {}Kg' .format(min(pesos)))
'''
'''
lista= []
for c in range (1,6):
    lista.append(int(input ('Qual o peso da {}ª pessoa? ' .format (c))))
print ('O maior peso é', max(lista))
print ('O menor peso é', min(lista))
'''

maiorpeso = 0
menorpeso = 0

for a in range(1,5):
    peso = float(input('{}°PESSOA - Digite peso: '.format(a)))
    #identifica maior peso
    if a == 1:
        maiorpeso = peso
    if peso > maiorpeso:
       maiorpeso  = peso
    # identifica menor peso
    if a == 1:
        menorpeso = peso
    if peso < menorpeso:
       menorpeso  = peso

print('O maior peso é {}Kg'.format(maiorpeso))
print('O menor peso é {}Kg'.format(menorpeso))





