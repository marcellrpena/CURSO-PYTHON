n2 = '1'
while n2=='1':
    print('Este programa calcula o desconto dado a um determinado produto.')
    produto = float(input('Digite o preço do produto: '))
    desconto = float(input('Digite o desconto do produto:'))
    desconto = produto*desconto/100
    n_preco =  produto - desconto
    print('o novo preço é: {}'.format(n_preco))
    n2 = input('digite 1 para continuar e 0 para sair:')
    if n2 == '0':
        print('Muito obrigado por utilizar o nosso serviço!!')
    while not (n2=='1' or n2=='0'):
        n2= input('opção errada, digite 1 para continuar e 0 para sair:')
