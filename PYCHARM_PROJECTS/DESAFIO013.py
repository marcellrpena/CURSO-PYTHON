n2 = '1'
while n2 =='1':
    print('Este programa calcula o novo salario \ndo seu funcionário com o novo reajuste:')
    salario = float(input('Digite o valor do seu salário: '))
    n3 = input('Para um reajuste positivo digite 1 \nPara um reajuste negativo digite 0: ')
    while not (n3=='1' or n3=='0'):
        n3 = input('Você digitou a opção errada, tente novamente: \nPara um reajuste positivo digite 1 \nPara um reajuste negativo digite 0 : ')
    if n3 == '1':
        reajuste = float(input('Digite a porcentagem do aumento salarial:'))
        reajuste = salario*reajuste/100
        n_salario = salario + reajuste
    if n3 == '0':
        reajuste = float(input('Digite a porcentagem do decremento salarial:'))
        reajuste = salario * reajuste / 100
        n_salario = salario - reajuste
    print('O seu antigo salário era: {} \nSeu novo salário é: {}'.format(salario,n_salario))
    n2 = input('digite 1 para continuar e 0 para sair:')
    if n2=='1':
        print('\n     \n    \n   ')
    if n2 == '0':
        print('Muito obrigado por utilizar o nosso serviço!!')
    while not (n2 == '1' or n2 == '0'):
        n2 = input('opção errada, digite 1 para continuar e 0 para sair:')
