print('oi' + "ola")  # junção de oi com ola
print('oi' * 5)  # oi será escrito 5 vezes
print('=' * 20)  # escreve o sinal de = , 20 vezes
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))  # escreve a entrada em 20 espaços
print('Prazer em te conhecer {:>20}'.format(nome))  # o sinal :> escreve a entrada em 20 espaços porém alinhado a
# direita
print('Prazer em te conhecer {:<20}'.format(nome))  # o sinal :< escreve a entrada em 20 espaços porém alinhado a
# esquerda
print('Prazer em te conhecer {:^20}'.format(nome))  # o sinal :^ escreve a entrada em 20 espaços porém alinhado no
# centro
print('Prazer em te conhecer {:=^20}'.format(nome))  # neste caso o sinal de = que aparece será o preenchimento o
#  circunflexo ^ será o tipo de alinhamento em que a entrada será posta e o 20 continua sendo a quantidade de espaço
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {}'.format(s, m, d))
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d))  # note que houve uma mudança nas chaves da divisão o .3f me
# permite imprimir um resultado com apenas 3 casas flutuantes, ou seja 3 casas antes do 0.
print('A divisão inteira é {}, e a potência é {}'.format(di, p))
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end= ' ')  # desta forma o próximo print ou
# linha será mostrada na tela na mesma linha anterior
print('A divisão inteira é {}, e a potência é {}'.format(di, p))
print('A soma é {} \no produto é {} \ne a divisão é {:.3f}'.format(s, m, d))  # o \n me permite quebrar uma linha dentro
# de um mesmo print


