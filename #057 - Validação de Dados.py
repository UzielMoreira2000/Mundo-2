'''
Exercício Python 057: Faça um programa que leia o sexo de
uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado, peça a digitação novamente até ter um valor correto.
'''


sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]

while sexo not in 'MF' :
      sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()
print('\n','='*30,'\nSexo {} registrado com sucesso'.format(sexo))











