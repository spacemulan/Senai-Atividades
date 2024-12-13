salario = float(input('Digite seu salário: '))

def aumento(salario):
    if salario<=280:
        reajuste= salario+(salario*0.2)
        print(f'Seu salário era R${salario:.2f}, ganhou um aumento de 20% e ficou R${reajuste:.2f}')
    elif salario>=280.01 and salario<=700:
        reajuste = salario+(salario*0.15)
        print(f'Seu salário era R${salario:.2f}, ganou um aumento de 15% e ficou R${reajuste:.2f}')
    elif salario>=700.01 and salario<=1500:
        reajuste = salario+(salario*0.1)
        print(f'Seu salário era R${salario:.2f}, ganhou um aumento de 10% e ficou R${reajuste:.2f}')
    else:
        reajuste = salario+(salario*0.05)
        print(f'Seu salário era R${salario:.2f} , ganhou um aumento de 5% e ficou R${reajuste:.2f} ')
aumento(salario)