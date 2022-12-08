'''
Exercício Python 043: Desenvolva uma lógica que leia o peso
e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

altura = float(input('Digite sua altura em(m):'))
peso = float(input('Digite seu peso em(Kg):'))

imc = peso/(altura**2)      # IMC é dado pelo peso dividido pelo quadrado da altura (que seria a area do corpo)
print('O IMC desse pessoa é de {:.1f}'.format(imc))

if imc < 18.5 :
    print('Sua classificação é Abaixo do Peso')
elif imc >= 18.5 and imc < 25  :
    print('Sua classificação é Peso Ideal')
elif imc  >= 25 and imc < 30  :
    print('Sua classificação é Sobrepeso')
elif imc >= 30 and imc < 40 :
    print('Sua classificação é Obesidade')
elif imc >= 40 :
    print('Sua classificação é Obesidade Mórbida')



