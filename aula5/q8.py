a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
operacao = input('Você quer subtrair, adicionar, multiplicar ou dividir? ')

if(operacao=='subtrair'):
    sub = a - b
    print(f'{a} - {b} = {sub} ')
elif(operacao=='adicionar'):
    add = a + b
    print(f'{a} + {b} = {add}')
elif(operacao=='multiplicar'):
    multi = a*b
    print(f'{a} x {b} = {multi}')
elif(operacao=='dividir'):
    divi = a/b
    print(f'{a} : {b} = {divi:.2f}')
else:
    print('Operação invalida!')