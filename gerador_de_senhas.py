#importar biblioteca de sorteio
import random
#Saudaçoes 
print('SEJA BEM VINDO AO SEU GERADOR DE SENHAS')
c=input('APERTE ENTER')
#Criar senha e mostrar
car=('ABCDEFGJHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%*&')
for c in range(0,8):
    print(car[random.randint(0,len(car))],end='')
print('FINALIZANDO PROGRAMA...')
