km = int(input('Qual distância você deseja percorrer? '))

def calc(km):
    if km <=200:
        calc= km *0.50
        print(f'O valor da viagem é R${calc:.2f}')
    else:
        calc = km *0.45
        print(f'Viagem mais longa, o valor da viagem é R${calc:.2f}')
    
calc(km)