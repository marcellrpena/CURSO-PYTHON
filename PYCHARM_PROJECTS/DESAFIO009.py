n2 = '1'
while n2 == '1':
    tabuada = int(input('Digite um número :'))
    stop = 1
    print('A tabuada de {} é:'.format(tabuada))
    while stop <= 10:
        resultado = tabuada*stop
        print('{} x {} = {}'.format(tabuada, stop, resultado))
        stop = stop + 1
    n2 = input('Deseja saber a tabuada de outro número? \nDigite 1 para sim \nou \nDigite 0 para não :')
    while not (n2 == '1' or n2 == '0'):
        n2 = input('Você digitou a resposta errada, por favor digite: \n1 para continuar \nou \n0 para sair :')
