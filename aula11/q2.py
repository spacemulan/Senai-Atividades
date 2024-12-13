turno = str.lower(input('Digite seu turno:'
              +' M para matutino'
              + ' V para respertino'
              + ' N para noturno: '))
def escolha(turno):
    if turno == 'm':
        print('Bom dia!!')
    elif turno == 'v':
        print('Boa tarde!!')
    elif turno =='n':
        print('Boa noite!!')
    else:
        print('Valor invalido!')
escolha(turno)