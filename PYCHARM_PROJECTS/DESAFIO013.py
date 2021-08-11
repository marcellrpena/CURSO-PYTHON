e2 = '1'
while e2 =='1':
    print('Este programa calcula o novo salario \ndo seu funcionário com o novo reajuste:')
    salario = float(input('Digite o valor do seu salário: '))
    e3 = input('Para um reajuste positivo digite 1 \nPara um reajuste negativo digite 0: ')
    while not (e3=='1' or e3=='0'):
        e3 = input('Você digitou a opção errada, tente novamente: \nPara um reajuste positivo digite 1 \nPara um reajuste negativo digite 0 : ')
    if e3 == '1':
        reajuste = float(input('Digite a porcentagem do aumento salarial:'))
        reajuste = salario*reajuste/100
        n_salario = salario + reajuste
    if e3 == '0':
        reajuste = float(input('Digite a porcentagem do decremento salarial:'))
        reajuste = salario * reajuste / 100
        n_salario = salario - reajuste
    print('O seu antigo salário era: {} \nSeu novo salário é: {}'.format(salario,n_salario))
    e2 = input('digite 1 para continuar e 0 para sair:')
    if e2=='1':
        print('\n     \n    \n   ')
    if e2 == '0':
        print('Muito obrigado por utilizar o nosso serviço!!')
    while not (e2 == '1' or e2 == '0'):
        e2 = input('opção errada, digite 1 para continuar e 0 para sair:')
