c=input('DESEJA VERIFICAR SE UMA PALAVRA É UM PALINDROMO OU NÃO?   ').upper()
if c[0]=='S':
    while c[0]=='S':
        p=[input('DIGITE UMA PALAVRA QUE IREI DIZER SE É UM PALÍDROMO:   ')]
        if p[-1:]==p[0:]:
            print(f'{p} é um palíndromo')
        else:
            (f'{p} não é um palíndromo')
        c=input('DESEJA CONTINUAR?     ').upper()
print('ENCERRANDO PROGRAMA...')
