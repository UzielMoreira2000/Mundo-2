
termos = 0
cont   = 0
s = 0
# laço infinito, interompido apenas pelo break
while True:
    n = int(input('Digite um numero :'))

    termos += n
    #laço é interompido caso a condição seja verdadeira
    if n == 999:
        break  # imterompe o while
    cont += 1
    s += n
print(f'Voce Digitou {cont} numeros, a soma dos numeros é {s}')
print('FIM')

'''==== Novo tipo de formatação ===== '''
print(f'Voce Digitou {cont} numeros, a soma dos numeros é {s:.2f}') # PYTHON 3.6 OU + Obs(lembrar do f antes das aspas)
print('Voce Digitou {} numeros, a soma dos numeros é {}'.format(cont,s)) # PYTHON 3.6 OU +
print('Voce Digitou %s numeros, a soma dos numeros é %d' % (cont,s))     # PYTHON 2 //Obs(Era nessessario colocar
                                                                         # o tipo do dado str=%s , int=%d)








