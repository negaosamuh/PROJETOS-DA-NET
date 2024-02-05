def linha():
    print('-='*30) 


linha()
print('SEJA BEM-VINDO Á CALCULADORA')
c=input('VAMOS CALCULAR?').upper()
linha()
while c[0]=='S':
        linha()
        n1=int(input('DIGITE O PRIMEIRO NUMERO:'))
        linha()
        n2=int(input('DIGITE O SEGUNDO NUMERO:'))
        linha()
        print('QUAL OPERAÇAO:')
        linha()
        print('[1] SOMA',end=''
            '[2] DIVISÃO',)
        print('[3] MULTIPLICAÇÃO',end=''
            '[4] SUBTRAÇÃO')
        linha()
        o=int(input('DIGITE UMA DAS OPÇÕES Á CIMA:  '))
        linha()
        if o==1:
            linha()
            print(f'{n1} + {n2} = {n1+n2}')
            linha()
        elif o==2:
            if n2==0:
                print('NÃO É POSSIVEL DIVIDIR POR ZERO(0)')
            else:
                linha()
                print(f'{n1} / {n2} = {n1/n2}')
                linha()
        elif o == 3:
            linha()
            print(f'{n1} * {n2} = {n1*n2}')
            linha()
        elif o == 4:
            linha()
            print(f'{n1} - {n2} = {n1-n2}')
            linha()
        c=str(input('DESEJA REALIZAR MAIS ALGUM CALCULO?')).upper()
linha()
print('FINALIZANDO PROGRAMA...')
linha()    
