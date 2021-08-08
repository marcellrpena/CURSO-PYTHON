n1 = input('Digite um número')
if n1.isnumeric():
    n1 = int(n1)
    ant = n1 - 1
    suc = n1 + 1
    print('O número digitado é {} \nseu antecessor é {} \nseu sucessor é {}'.format(n1, ant, suc))
else:
    print('O valor digitado não corresponde a um número inteiro')
