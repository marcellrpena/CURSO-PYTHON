nome = input('digite o seu nome:  ')
print('Seja bem vindo, ', nome, '  !!!',
      'esta primeira mensagem foi criada usando a sintaxe: (texto, variavel, texto)')
# dessa forma consigo deixar comentario no script
print('Seja bem vindo, ' + nome + '!!, esta segunda mensagem foi criada '
                                  'usando a sintaxe: (texto + variavel+ texto)')
# no python nós temos a saída formatada, é usado um bloco '{}'
# dentro do texto das aspas e logo após as aspas não se usa virgula
# usamos a função .format(nome da variável)
print('é um prazer te conhecer, {}!'.format(nome))
