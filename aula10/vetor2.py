#crie um algoritmo que recebe 6 numeros e armazena em um vetor 
# e a função vai armazenar e mostrar só os impares

vetor = []
contador = 0

def armazena(vetor, contador):
    for _ in range(6):
        contador = contador +1
        x =  int(input(f'{contador} Digite número: '))
        vetor.append(x)
    for x in vetor:
        if x % 2 == 1:
            print(x)
armazena(vetor,contador)