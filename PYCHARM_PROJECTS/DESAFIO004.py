n = input("Digite algo:")
if n.isalpha() == False and n.isalnum() == False and n.isnumeric() == False:
    print('não foi digitado nenhum valor ou os parâmetros não foram atendidos')
if not n.isalpha() == False and n.isalnum() == False and n.isnumeric() == False:
    print('é alpha numérico? {}, '
      'são letras? {}, é numérico? {}'.format(n.isalnum(), n.isalpha(), n.isnumeric()))
if n.isnumeric():
    print('o valor digitado contpem apenas números')
if n.isalpha():
    print('o valor digitado contém apenas letras')
if n.isalnum() and n.isalpha() == False and n.isnumeric() == False:
    print('o valor digitado provavelmente contém letras e números')

# na linha acima temos
# 'isalnum'= alpha numerico, letras e numeros ou maiuscula e minuscula
# 'isalpha'= alpha ou seja se é apenas letra
# 'isnumeric'= se o valor recebido é numerico ou não
# para todos esses tipos a saída será booleana, ou seja, true ou false
