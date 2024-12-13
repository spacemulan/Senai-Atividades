peixes = int(input('Digite o peso de peixes: '))


def calc(peixes):
    if peixes>50:
        excedente = peixes - 50        
        multa = excedente*4
        print(f'A multa a ser pagar é R${multa:.2f}')
    else:
        print('Você não pagará multa!')
calc(peixes)
    
