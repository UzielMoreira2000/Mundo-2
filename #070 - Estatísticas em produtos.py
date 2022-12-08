'''
Exercício Python 070: Crie um programa que leia o nome
e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

cont1 = 0
ac = 0
cont = 0
nome = ' '
print('=' * 25, '\n  SUPERMERCADO SUPER BARÃO\n', end='='* 25)
menor = 0
nomemenor = ''

while True:

    print(f'\n', '-' * 13, f'\n  {cont+1}° Produto\n', '-' * 13)
    preço = int(input('Preço do produto: '))
    nome = str(input('Produto : ')).strip().upper()[0]
    ac += preço
    cont += 1
    cond = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]

    # condicao para produtos com valor maior que R$1000
    if preço >= 1000:
        cont1 += 1

    if cont == 1:
        menor = preço

    if preço < menor:
        menor = preço
        nomemenor = nome

    if cond in 'N':
        print('\nPrograma Encerrado')
        print(f'O total da compra foi R${ac:.2f}')
        print(f'Foram comprados {cont1} produtos com valor maior que R$1000')
        print(f'O nome do produto mais barato é {nomemenor} e custa R${menor:.2f}')

        break

    if cond != 'S' and cond != 'N':
        print('\nOpção não reconhecida')
        cond = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]













