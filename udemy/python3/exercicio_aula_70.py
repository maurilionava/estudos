frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i_letra_atual = 0
letra_destaque = ''
qtde_vezes = 0

while i_letra_atual < len(frase):
    if frase[i_letra_atual] != ' ' and frase.count(frase[i_letra_atual]) > qtde_vezes:
        qtde_vezes = frase.count(frase[i_letra_atual])
        letra_destaque = frase[i_letra_atual]

    i_letra_atual += 1

print(f'A letra que mais apareceu foi "{letra_destaque}", tendo aparecido {qtde_vezes} vez(es)')
