n1 = input('Digite o primeiro número:')
while not n1.isnumeric():
    print('O valor digitado não é valido ou não corresponde a um número')
    n1 = input('Digite novamente o número:')
n1 = int(n1)
n2 = input('Digite o segundo número:')
while not n2.isnumeric():
    print('O valor digitado não é valido ou não corresponde a um número')
    n2 = input('Digite novamente o número:')
n2 = int(n2)
print('A soma entre {} e {} é : {}'.format(n1, n2, n1+n2))
