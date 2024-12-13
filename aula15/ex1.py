kms = int(input('Digite a velocidade percorrida: '))

if kms > 80:
    excedente = kms - 80
    multa = excedente*5
    print(f'Limite ultrapassado, você vai pagar uma multa de R${multa:.2f}')
else:
    print('Você não ultrapassou a velocidade máxima, não há multa.')