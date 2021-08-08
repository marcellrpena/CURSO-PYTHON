n2 = '1'
while n2 == '1':
    print('Bem-vindo ao gestor de pintura, \nvamos calcular a área e a quantidade de tinta para pintar a sua parede')
    largura = float(input('Digite a largura da parede em metros: '))
    altura = float(input('Digite a altura da parede em metros: '))
    area = largura * altura
    tinta = area // 2
    print('A área total da sua parede é: {} \nA quantidade de tinta necessária para pintar a parede é: {}'
          .format(area, tinta))
    n2 = input('Para fazer um novo calculo digite 1, para sair digite 0:')
    while not (n2 == '1' or n2 == '0'):
        print('Você digitou a opção errada \nDigite 1 para um novo calculo \nou \nDigite 0 para sair.')
        n2 = input('opção: ')
