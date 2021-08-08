print('Esse programa calcula a sua média')
quant = int(input('Digite a quantidade de notas:'))
stop = 1
dividendo = 0
# enquanto a condição for atendida
# pergunta o valor de todas as médias e soma todas elas para formar o dividendo
while stop <= quant:
    nota = float(input('Digite a {} nota: '.format(stop)))
    dividendo= nota + dividendo
    stop = stop + 1
media = dividendo / quant
print('A média das {} notas que você digitou é : {:.3f} '.format(quant, media))

