#1) Questão: Escreva um programa que converte uma temperatura 
# dada em graus Fahrenheit para Celsius. Use a fórmula: C*=(F-30)/2
f= int(input('Digite uma temperatura em Fahrenheit: '))
c=(f-30)/2
print(f'A temperatura em Celsius é {c:.0f}°')