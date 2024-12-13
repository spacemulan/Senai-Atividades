n1 = float(input('Digite a nota da primeira unidade: '))
n2 = float(input('Digite a nota da segunda unidade: '))
n3 = float(input('Digite a nota da terceira unidade: '))

media = (n1+n2+n3)/3

if media>=7:
    print(f'Sua média foi {media: .1f} , você foi aprovado')
elif media>=5 and media<=6.9:
    print(f'Sua média foi {media: .1f} , você foi para a recuperação')
else:
    print('Sua média foi {media: .1f}, você foi reprovado')