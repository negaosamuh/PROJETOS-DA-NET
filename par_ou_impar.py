def linha():
    print('-='*30)


c=str(input('DESEJA VERIFICAR SE UM NUMERO É IMPAR OU PAR?    [S/N]:   ')).upper()
n=0
if c == 'S':
    while c=='S':
        n=int(input('DIGITE UM NUMERO INTEIRO QUE IREI VERIFICAR SE ESTE NUMEROP É IMPAR O PAR:    '))
        if n %2==0:
            linha()
            print(f'O NUMERO {n} É PAR')
            linha()
        else:
            linha()
            print(f'O NUMERO {n} É ÍMPAR')
            linha
        c=str(input('DESEJA CONTINUAR?    [S/N]:   ')).upper()
print('SAINDO DO PROGRAMA...')
