peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

def imcs(peso, altura):
    
    imc = peso/(altura*altura)
    if(imc<=16.9 and imc<=18.4):
        print(f'Seu imc é {imc:.1f} você está abaixo do peso')
    elif(imc>=19.5 and imc<=24.9):
        print(f'Seu imc é {imc:.1f}, você está com o peso normal')
    elif(imc>=25 and imc<=29.9):
        print(f'Seu imc é {imc:.1f}, você está acima do peso')
    elif(imc>=30 and imc<35):
        print(f'Seu imc é {imc:.1f}, você está com obesidade grau I')
    else:
        print(f'Seu imc é {imc:.1f}, você está com obesidade grau II')
        
imcs(peso,altura)   