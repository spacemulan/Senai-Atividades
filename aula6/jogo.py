import random

secreto = random.randint(1,100)
contador = 0
while True:
    valor = int(input('Digite um numero secreto: '))
    contador = contador +1
    if(valor==secreto):
        print(f'Você acertou o número secreto após {contador} tentativas')
        break
    elif(valor>secreto):
        print('O número secreto é menor')
    else:
        print('O numero secreto é maior')