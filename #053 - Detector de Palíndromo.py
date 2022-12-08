'''
Exercício Python 046: Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
'''


f = str(input('digite uma frase:')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print('\n',f,'| fica ->',inverso)
if inverso == junto:
    print('\nEntão temos um palíndromo')
else:
    print('\nA frase digitada nao é um palíndromo')




