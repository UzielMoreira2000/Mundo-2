'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date      # importando a data na  biblioteca de data time

ano = int(input('Ano de nascimento:'))
anoatual = date.today().year
idade = anoatual-ano

print('Quem nasceu em {} tem {} anos de idade em {}'.format(ano,idade,anoatual))

if idade <=9 :
    print('Sua classificação é MIRIM')

elif idade  <= 14 and idade > 9  :
    print('Sua classificação é INFANTIL')

elif idade  <= 19 and idade > 14  :
    print('Sua classificação é JÚNIOR')

elif idade <= 25 and idade > 19  :
    print('Sua classificação é SÊNIOR')

elif idade >= 25 :
    print('Sua classificação é MASTER')










