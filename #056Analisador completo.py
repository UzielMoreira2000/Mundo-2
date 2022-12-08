'''
Exercício Python 056: Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.

    peso = float(input('Digite o peso: '))
'''
cont = 0
velho = ''
maioridadehomem = 0
mulheresnovas= 0

for c in range (1,5):
    print('-'*6,'{}°PESSOA'.format(c),'-'*12)
    nome  = str(input('Nome:')).upper().strip()
    idade = int(input('idade:'))
    sexo  = str(input('sexo [M/F]:')).upper().strip()
    cont += idade
    #identifica a idade do homem mais velho
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        velho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        velho = nome
    # identifica mulheres menores de 20 anos
    if idade < 20 and sexo in 'Fm':
        mulheresnovas += 1

media = cont/4
print('A media de idade é:{:.0f}'.format(media))
print('O homem mais velho tem {}anos e se chama {}, {} mulheres sao menores de idade'
      .format(maioridadehomem,velho,mulheresnovas))








