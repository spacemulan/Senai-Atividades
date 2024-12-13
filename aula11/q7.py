km = int(input('Digite os kms percorridos: '))
dias = int(input('Digite os dias de aluguel do carro: '))

def prec(km, dias):
    kms = km*0.15 
    dia = dias*60
    preco = kms+dia
    print(f'O preço a pagar é R${preco:.2f}')
prec(km,dias)