time = input('Digite o time: ')
pontos = int(input('digite a sua pontuação final: '))

if(pontos<45):
    print(f'O {time} corre risco de rebaixamento!')
elif(pontos>45 and  pontos<=55):
    print(f'O {time} tem chances de sul-americano!')
elif(pontos>55 and pontos<=62):
    print(f'O {time} tem grandes chances de libertadores')
else:
    print(f'O {time} tem grandes chances de titulo!')