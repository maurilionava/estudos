nome = input('Digite seu nome: ')
idade_str = input('Digite sua idade: ')
#if(nome == '' and idade_str == ''):
if(nome and idade_str):
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    # print(f'Seu nome invertido é {nome[-1::-1]}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém (ou não) espaços {' ' in nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')