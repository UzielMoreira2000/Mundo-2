'''
Exercício Python 039: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou se
já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
'''
from datetime import date      # importando a data na  biblioteca de data time

ano = int(input('Ano de nascimento:'))

anoatual = date.today().year
idade = anoatual-ano

idadefaltante= 18-idade

anodealistamento = anoatual+idadefaltante

tempopassado = idade-18

anoquedeveriasealistar = anoatual - tempopassado

print('Quem nasceu em {} tem {} anos de idade em {}'.format(ano,idade,anoatual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento\n'
          'Seu alistamento será em {}'.format(idadefaltante,anodealistamento ))

elif idade == 18 :
    print('Parabens voce pode se alistar apartir desse ano!')

elif idade > 18 :
    print('O senhor ja deveria ter se alistado á {} anos!'
             '\nSeu alistamento deveria ter sido em {}'
             .format(tempopassado ,anoquedeveriasealistar ))







