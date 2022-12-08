'''
Exercício Python 054: Crie um programa que leia o
 ano de nascimento de 5 pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date

anoatual = date.today().year
menor = 0
maior = 0
for c in range(1, 6):
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    idade = anoatual - ano
    if idade <= 18 :
        menor += 1
    else:
        maior += 1
print('sao {} pessoas  menores de idade'.format(menor))
print('sao {} pessoas maiores de idade'.format(maior))