'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

r1= int(input('digite um valor para uma reta:'))
r2= int(input('digite outro valor para uma reta:'))
r3= int(input('digite outro valor para uma reta:'))

# classificaçao dos triangulos só existe se eles forem formados

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
   print('\nÉ possivel formar um Triangulo')
   if r1 == r2 and r2 == r3 and r3 == r1:
       print('\nEsse triangulo é EQUILÁTERO')
   if r1 != r2 and r2 != r3 and r3 != r1:
       print('\nEsse triangulo é ESCALENO ')
   else:
       print('\nEsse triangulo é ISÓSCELES')
else:
    print('\nNao é possivel formar um Triangulo')


