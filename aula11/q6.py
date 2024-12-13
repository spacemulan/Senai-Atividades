

total_eleitores=int(input('Digite quantos eleitores tem cada candidato: '))
datena =0
marcal = 0
boulos = 0

for x in range(total_eleitores):
    voto = input('Escolha candidatos: D, M e B ')
    if voto == 'd':
        datena = datena + 1
    elif voto == 'm':
        marcal = marcal + 1
    elif voto == 'b':
        boulos == boulos +1
    else:
        print('Voto nulo!')

if datena>marcal and datena>boulos:
    print('O datena venceu')
elif boulos>datena and boulos>marcal:
    print('O boulos venceu')
elif marcal>boulos and marcal>datena:
    print('O Marçal venceu!')
elif boulos==marcal and boulos>datena and marcal>datena:
    print('Empate tecnico entre Boulos e Marçal')
elif boulos==datena and datena>marcal and boulos>marcal:
    print('Empate tecnico Boulos e Datena')
elif marcal==datena and datena>boulos and marcal>boulos:
    print('Empate tecnico entre Marçal e Datena')
else:
    print('Empate tecnico entre Boulos, Marçal E Datena')