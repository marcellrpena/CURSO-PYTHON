valor = input('Digite qualquer coisa: ')
if valor.isalpha and valor.isnumeric():  # se o valor contém letras e números
    print("O valor digitado CONTÉM letras e números")
else:
    print('O valor digitado NÃO CONTÉM letras e números')
if valor.isnumeric():  # se o valor contém apenas números
    print('O valor digitado CONTÉM apenas números')
else:
    print('O valor digitado NÃO CONTÉM apenas números')
if valor.istitle():  # se o valor contém a primeira letra maiúscula
    print('O valor digitado TEM a sua primeira letra MAIÚSCULA')
else:
    print('O valor digitado NÃO TEM a sua primeira letra MAIÚSCULA')
if valor.isalpha():  # se o valor contém apenas letras ou seja alfabético
    print('O valor digitado CONTÉM APENAS letras')
else:
    print('O valor digitado NÃO CONTÉM APENAS letras')
if valor.islower():  # se o valor contém apenas letras minúsculas
    print('O valor digitado CONTÉM TODAS AS LETRAS MINÚSCULAS')
else:
    print('O valor digitado NÃO CONTÉM TODAS AS LETRAS MINÚSCULAS')
if valor.isupper():  # se o valor contém apenas letras maiúsculas
    print('O valor digitado CONTÉM TODAS AS LETRAS MAIÚSCULA')
else:
    print('O valor digitado NÃO CONTÉM TODAS AS LETRAS MAIÚSCULA')
if valor.isspace():  # se o valor contém,apenas espaço
    print('O valor digitado CONTÉM apenas ESPAÇO')
else:
    print('O valor digitado NÃO CONTÉM apenas ESPAÇO')
