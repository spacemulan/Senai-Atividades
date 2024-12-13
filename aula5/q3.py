temperatura = int(input('Digite uma temperatura: '))

if(temperatura<15):
    print('Está frio!')
elif(temperatura>15 and temperatura<=25):
    print('Está agradável!')
else:
    print('Está quente!')