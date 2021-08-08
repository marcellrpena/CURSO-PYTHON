n1 = input('Digite um valor: ')
print(type(n1))
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
# print('A soma entre', n1, 'e', n2, 'é: {}'.format(n1+n2))
# a forma escrita abaixo é mais simples de ser escrita e evita
# muitas linhas de código
print('A soma entre {} e {} vale: {}'.format(n1, n2, n1 + n2))
print(type(n1))
n = input("Digite algo:")
print(n.isalnum(), n.isalpha(), n.isnumeric())
# na linha acima temos
# 'isalnum'= alpha numerico, letras e numeros ou maiuscula e minuscula
# 'isalpha'= alpha ou seja se é apenas letra
# 'isnumeric'= se o valor recebido é numerico ou não
# para todos esses tipos a saída será booleana, ou seja, true ou false
