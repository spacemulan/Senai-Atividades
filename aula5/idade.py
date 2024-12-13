idade = int(input('digite sua idade: '))

if(idade<=12):
    print('Voce é uma crianca')
elif(idade>12 and idade<=17):
    print('Voce é um adolescente')
elif(idade>17 and idade<=60):
    print('Você é adulto!')
else:
    print('Você é idoso!')