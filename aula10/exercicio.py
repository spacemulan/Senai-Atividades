#crie um algoritmo qu recebe o nome de 10 times
#de futebol e sorteia qual será o campeão

import random

times = []
contador = 0


for x in range(10):
    contador = contador + 1
    nomes = input(f'{contador}.Digite um time: ')
    times.append(nomes)

def sorteio(times):
    print('O time vencedor foi: ' + random.choice(times))
sorteio(times)