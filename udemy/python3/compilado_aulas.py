# Hello World Python
print('Hello World!')

"""
Informações Gerais
    um módulo python é todo arquivo com extensão .py
    tipagem dinamica e forte (não converte o tipo automaticamente)
    r e escape
    tudo em python é um objeto
    carregar módulo python no powershell com o comando -i nome_arquivo.py para testar variáveis
    variáveis servem para deixar o código mais legível, usar sem medo
    CONSTANTE - convenção
    evitar muitas condições no mesmo if devido ao aumento da complexidade

Tipos de dados primitivos  
    int
    float
    str
    bool
  
Conversão de tipos
    int(x)
    float(x)
    str(x)
    bool(x)

Operadores aritméticos
    + soma
    - subtração
    * multiplicação (inclusive com strings por exemplo: 'print(python * 3)')
    / divisão
    // divisão inteira
    ** exponenciação
    % módulo

Operadores relacionais (de comparação)
    >   maior
    >=  maior ou igual
    <   menor
    <=  menor ou igual
    ==  igual
    !=  diferente

Operadores de atribuição
    =
    +=
    -=
    *=
    /=
    //=
    **=
    %=
    
Precedência de operadores aritméticos
    1. ()
    2. **
    3. * / // %
    4. + -
    
Funções
    print() - imprimir dados na tela
    len() - retornar o tamanho da string
    id() - ? verificar o identificador da variável na memória
    input() - receber dado digitado pelo usuário no terminal em formato str
    string.count(x) - verificar quantidade de vezes que termo aparece na string

Classes
    type()

Formatação de strings
    f-strings
        f'string qualquer com uma {var_str} e {valor_reais:,.2f}'

    Fatiamento de strings
        variavel[i:f:p] = str_var[4:] ou str_var[:4]
"""

# formatação de strings com .format
a=0; b=1; c=2 # declaração das variáveis
formato = 'a={0} a={0} b={1:.2f} c={2:.2f}'.format(a, b, c)
formato = 'a={var_1} a={var_1} b={var_2:,.2f} c={var_3:.2f}'.format(var_1=a, var_2=b, var_3=c) #parametro nomeado

#44 interpolação de string com %
"""
s - string 
d e i - int 
f - float 
x e X - hexadecimal(ABCDEF0123456789)
"""
nome = 'John Doe'
valor = 123.45
aux = '%s, o preço é R$ %.2f' % (nome, valor)
print(aux)
aux = 1500
print('O hexadecimal de %i é %X' % (aux, aux))

# condicionais if elif else
if True:
    ...
elif False:
    ...
elif False:
    ...
elif False:
    pass
else:
    ...

#operadores lógicos
"""
and or not
falsy values valores falsos
0 0.0 '' False None (não valor)
"""
if True and True:
    ...
elif True or False:
    ...
elif not False:
    ...
elif not True:
    ...
#avaliação de curto circuito
elif True and False and True:
    ...

# in e not in
xpto = 'xpto'
aux = 'xp' in xpto # True
aux = '1' in xpto # False
print('-' * 10)
aux = 'xp' not in xpto # False
aux = '1' not in xpto # True

#49 try...except para capturar erros (exceptions)
try:
    ...
except Exception as error:
    print(error)

# while laço de repetição
condicao = True

while condicao:
    break
    continue
    ...

while condicao:
    break
    continue
    ...
else:
    print('Sera impresso se nao houver instruçao break no laço while')

# 72 for in
palavra = 'xpto'

for letra in palavra:
    print(letra)

# 73 for range
# range(start, stop, step)
numeros = range(10) # 1:10 range(0,10)
numeros = range(5, 10) # 5:10 range(5,10)
numeros = range(5, 10, 2) # 5:10 range(5,10,2)

for numero in numeros:
    print(numero)

# 74 iterável & iterador & __iter__
# 'dumder' iter
    
# 75 for else break continue
for(numero) in numeros:
    print(numero)

    if numero == 1:
        continue

    if numero == 2:
        break
    
else:
    print('For completo com sucesso')