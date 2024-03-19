palavra = 'python'

input_usuario = ''
palavra_secreta = ''

while True:
    input_usuario = input('Digite uma letra: ')

    if len(input_usuario) > 1:
        print('Digite apenas uma letra: ')
        continue

    palavra_secreta = ''

    for letra in palavra:
        if letra == input_usuario:
            palavra_secreta += f'{letra}'
        else:
            palavra_secreta += '*'

    print(f'{palavra_secreta}')