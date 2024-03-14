from database import db,Usuario
from time import sleep
from getpass import getpass

db.connect()

db.create_tables([Usuario])


print('_'*35)
print()
print('BEM - VINDO AO NOSSO SISTEMA !!!')
print('_'*35)

#Função para fazer o login
def login():
    #Pega email e senha digitado pelo usuario
    get_email = str(input('Digite seu email : '))
    get_senha = getpass('Digite sua senha: ')

    #Seleciona a Tabalea usuario e pegar na tabela usuario o campo email 
    usuarios = Usuario.select().where(Usuario.email == get_email).first()

    if usuarios:
        if get_senha == usuarios.senha:
            print()
            print('Fazendo login ...')
            sleep(2)
            print('Login bem-sucedido !!!')
            print()
            print(f'BEM VINDO AO NOSSO SISTEMA !!!')
        else:
            print('email ou senha incorretos. Tente novamente')
    else:
        print('Email não encontrado. Tente novamente')

#Função para realizar um cadastro
def cadastro():
    nome = str(input('Digite seu nome : '))
    email = str(input('Digite seu melhor email : '))
    senha = getpass('Digite sua senha : ')

    #Verifica se o usuario digitou nome, senha, email com mais de 5 caracteres
    if len(nome) < 5 or len(email) < 5  or len(senha) < 5:
        print('*'*50)
        print()
        print('Os campos nome, email e senha tem que possuir mais de 5 caracteres !!!')
        print()
        print('*'*50)

    print('Cadastrando novo usuario ....')
    sleep(2)
    Usuario.create(nome = nome, email = email, senha = senha)
    print('Usuario Cadastrado com sucesso !!!')

#Função para criar o menu 
def menu():
    while True:
        print()
        print('Selecione a opção desejada !!!')
        print()
        print('[ 1 ] - Fazer login')
        print('[ 2 ] - Fazer Cadastro')
        print('[ 3 ] - Sair do sistema')
        print()
        
        opcao = int(input('Digite a opção desejada : '))

        if opcao == 1 : 
            login()
        if opcao == 2 :
            cadastro()
        if opcao == 3:
            print('Saindo do sistema ....')
            sleep(2)
            break
menu()