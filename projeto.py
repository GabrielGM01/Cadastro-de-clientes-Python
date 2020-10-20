from datetime import datetime

def tela():
    print('-----------------------------------------------------------------------')
    print('Digite uma das opções')
    print('Digite 1 para realizar o cadastro')
    print('Digite 2 para verificar cadastro')
    print('Digite 3 para deletar cadastro')
    print('-----------------------------------------------------------------------')
    n = input()
    if (n == '1'):
        cadastro()
    elif(n == '2'):
        verificar()
    elif(n == '3'):
        deletar_cadastro()
    else:
        tela()

    


def deletar_cadastro():
    cpf = input(str("Digite o CPF:"))
    with open("dados.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if cpf not in line:
                f.write(line)
        f.truncate()
        print('Cadastro deletado com sucesso')
        tela()
    
    

def verificar():
    cpf = input(str("Digite o CPF:"))
    arquivo = open('dados.txt', 'r')
    for linha in arquivo: 
        if cpf in linha:
            print(linha)
    arquivo.close()
    tela()
            

                        


def cadastro():
    nome = input(str('Digite o nome:'))
    cpf  = input(str('Digite o cpf:'))
    idade = input(str('Digite idade:'))
    data_cadastro = datetime.now()
    arquivo = open("dados.txt", "a")
    arquivo.write('Nome:{} CPF:{} Idade:{} Cadastro:{}\n'.format(nome,cpf,idade,data_cadastro))
    arquivo.close()
    print('Cadastro feito com sucesso')
    tela()


tela()


