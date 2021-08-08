carteira = int(input('Quanto você tem na sua carteira: '))
cotação = float(5.18)
dolar = carteira // cotação
print('Você pode comprar com {} reais na cotação atual de {} dolares a quantia de : {} dolares '.format(carteira, cotação, dolar))