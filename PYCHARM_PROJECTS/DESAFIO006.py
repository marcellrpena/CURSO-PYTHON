# estou alocando um valor string na variável n2 porque estou prevendo que o cliente pode errar na digitação quando
# for requisitado uma entrada
n2 = '1'
# como estou trabalhando com string a comparação entre aspas compara a string '1' e não o numero inteiro 1
# enquanto a condição for aceita o cliente poderá rodar o programa
while n2 == '1':
    n1 = input('Digite um número inteiro: ')
    # se o valor que o cliente digitar não for numérico o erro será relatado e exigido uma nova entrada
    # enquanto a condição não for atendida o loop não será quebrado
    while not n1.isnumeric():
        n1 = input('Isso não é um número \nMuito menos inteiro \npor favor digite novamente:')
    n1 = float(n1)
    dobro = n1 * 2
    triplo = n1 * 3
    rq = n1**( 1 /2)
    print("O numero digitado foi o : {} \nO dobro do número é: {} \nO triplo do número é: {} \nA raiz quadrada deste "
          "número é: {}".format(n1, dobro, triplo, rq))
    n2 = input('Deseja continuar? aperte o número 1 \nPara sair aperte o número 0 : ')
    # caso a entrada que o cliente digitar for diferente de '0' ou '1' como string será emitido uma mensagem de erro
    # pedindo ao cliente para digitar novamente a entrada correta.
    # enquanto a condição não for atendida o loop não será quebrado
    while not (n2 == '0' or n2 == '1'):
            n2 = input('Você digitou o número errado \nAperte 1 para continuar \nOu \n0 para sair:')

