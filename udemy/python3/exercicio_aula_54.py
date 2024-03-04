# Exercício 1
input_usuario = input('Digite um número inteiro: ')

if input_usuario.isdigit():
    input_usuario_int = int(input_usuario)

    if input_usuario_int % 2 == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é ímpar')
else:
    print('O valor digitado não é um número inteiro')

# Exercício 2
input_usuario = input('Informe a hora do dia: ')

if input_usuario.isdigit():
    input_usuario_int = int(input_usuario)

    if(input_usuario_int >= 0 and input_usuario_int <= 11):
        print('Bom dia caro usuário')
    elif(input_usuario_int <= 17):
        print('Boa tarde caro usuário')
    else:
        print('Boa noite caro usuário')

# Exercício 3
input_usuario = input('Digite seu primeiro nome: ')
tamanho_nome_usuario = len(input_usuario)

if(tamanho_nome_usuario <= 4):
    print('Seu nome é curto')
elif(tamanho_nome_usuario <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')