from time import sleep
from funcoes import verificar, cadastro, deletar_cadastro, cls


n = 0

while n != '4':
    print('''
-----------------------------------------------------------------------
Digite uma das opções
[1] para realizar o cadastro
[2] para verificar cadastro
[3] para deletar cadastro
[4] para sair
-----------------------------------------------------------------------
         ''')
    n = input()
    if (n == '1'):
        cadastro()
        sleep(3)
        cls()
    elif(n == '2'):
        verificar()
        input("Pressione <enter> para continuar")
        cls()
        
    elif(n == '3'):
        deletar_cadastro()
        sleep(3)
        cls()
    elif(n == '4'):
        print('finalizando...')
        sleep(3)
        cls()
    else:
        print('Opção inválida. tente novamente')
        sleep(3)
        cls()

    





