vetor = []
contador = 0
for x in range (5):
    contador = contador + 1
    num = int(input(f'{contador}. Digite um numero: '))
    vetor.append(num)
print(vetor)    
soma = sum(vetor)
media = soma / 5
print(f'A soma dos números é {soma}, a média é {media:.1f}')