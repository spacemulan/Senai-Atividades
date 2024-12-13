# while True:
#     valor = input('Digite alguma coisa que não seja exit: ')
#     if(valor=='exit'):
#         break
#     else:
#         print(valor)

#crie um algoritimo que pergunta para voce um numero
# e lhe diz se esse numero é par ou irmpar, o sistema
# para se o numero que você digitar for zero


while True:
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        print('Numero par')
    elif(valor==-1):
        break
    else:
        print('numero impar')

