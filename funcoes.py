#IMPORTAR BIBLIOTECA PARA PUXAR DATA E HORA 
from datetime import datetime     
import os                         

#limpar o historico do programa (clean)
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #limpar o terminal


def deletar_cadastro():
    n1 = 1
    #Verificar CPF
    while n1 != 0:                          
        cpf = input(str("digite o CPF:"))
        #O try  permite testar um bloco de código
        try:
            cpf = int(cpf)
            if type(cpf) == int:
                cpf = str(cpf)
                if type(cpf) == str:
                    n1 = 0
        #O except  permite lidar com o erro.
        except:
            print("CPF inválido")
    #O (+) siginifica  atualizar tanto leitura quanto escrita        
    with open("dados.txt","r+") as dado:  
        #retorna o todo o conteúdo do arquivo em uma lista de string
        novo_dado = dado.readlines()      
        #cada item da lista representa uma linha do arquivo, posiciona o cursor no inicio do arquivo
        dado.seek(0)
        #se o cpf não estiver no novo dado criado ele copia para o arquivo principal assim atualizando
        for linha in novo_dado:
            if cpf not in linha:
                dado.write(linha)
        #Não entendi mas resolveu o problema
        dado.truncate()
        print('Cadastro deletado com sucesso')
     
def verificar():
    t = 1
    n1 = 1
    #Verificar CPF
    while n1 != 0:                          
        cpf = input(str("digite o CPF:"))
        #O try  permite testar um bloco de código
        try:
            cpf = int(cpf)
            if type(cpf) == int:
                cpf = str(cpf)
                if type(cpf) == str:
                    n1 = 0
        #O except  permite lidar com o erro.
        except:
            print("CPF inválido")   
    arquivo = open('dados.txt', 'r')
    for linha in arquivo: 
        if cpf in linha:
            print(linha)
            t = 0
    arquivo.close()
    if t == 1:
        print("CPF não encontrado")
        
def cadastro():
    t = 1
    n1 = 1
    n2 = 1
    nome = input(str('Digite o nome:'))
    #Verificar CPF
    while n1 != 0:                          
        cpf = input(str("digite o CPF:"))
        #O try  permite testar um bloco de código
        try:
            cpf = int(cpf)
            if type(cpf) == int:
                cpf = str(cpf)
                if type(cpf) == str:
                    n1 = 0
        #O except  permite lidar com o erro.
        except:
            print("CPF inválido")
    while n2 != 0:
        idade = input(str("digite a idade:"))
        try:
            idade = int(idade)
            if type(idade) == int:
                idade = str(idade)
                if type(idade) == str:
                    n2 = 0
        except:
            print("Idade inválido")
    #Armazenar na variavel a data e hora do cadastro        
    data_cadastro = datetime.now()

    #Abrindo o arquivo no modo leitura (r)
    arquivo = open('dados.txt', 'r')    

    #Criando uma variavel para navegar entre as linhas do arquivo
    for linha in arquivo:

        #Se a variavel cpf digitada estiver no arquivo retorna para o usuário cpf ja cadastrado
        if cpf in linha:                
            print("CPF ja Cadastrado")
            #Se o CPF ja estiver cadastrado a variavel (T) recebe 0 para não iniciar o processo de cadastro
            t = 0
    #Fechamento do arquivo        
    arquivo.close()                     
    #Abrindo o arquivo no modo Escrita (a)
    arquivo = open("dados.txt", "a")    
    if t == 1:
        #método(write)recebe uma string como parâmetro e a insere no arquivo
        arquivo.write('Nome:{} CPF:{} Idade:{} Cadastro:{}\n'.format(nome,cpf,idade,data_cadastro)) 
        print('Cadastro feito com sucesso')    
    #Fecha o arquivo
    arquivo.close()                         


           
    
