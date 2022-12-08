'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão: 1
para binário, 2 para octal e 3 para hexadecimal.
'''
n = int(input('Digite o número que deseja converter:'))

base = int(input('Escolha uma das bases para conversao:\n'
      '[1] para converter para binario\n'
      '[2] para converter para octal\n'
      '[3] para converter para hexadecimal:'))

if base == 1 :
   print('\nO número {} em binário é: {}'.format(n,bin(n)[2:]))
if base == 2 :
    print('\nO número {} em octal é: {}'.format(n,oct(n)[2:]))
if base == 3 :
    print('\nO número {} em hexadecimal é: {}'.format(n,hex(n)[2:]))
else:
    print('\nA opcao de converção não existe, tem novamente')

