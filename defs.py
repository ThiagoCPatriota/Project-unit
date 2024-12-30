from database import Usuario, Conta, db

db.connect()
db.create_tables([Usuario, Conta])

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")


    try:
        Usuario.create(nome=nome, telefone=telefone, email=email, senha=senha)
        Conta.create(usuario=email, saldo=0)
        print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")

def deposito():
    email = input('Digite seu Email: ')
    senha = input('Digite sua senha: ')

    try:
        usuario = Usuario.get((Usuario.email == email) & (Usuario.senha == senha))

        conta = Conta.get(Conta.usuario == email)
        valor = float(input('Digite o valor do deposito: '))

        conta.saldo += valor
        conta.save()

    except Usuario.DoesNotExist:
        print(f'Usuario não encontrado ou senha Incorreta!')
    except Exception as e:
        print(f'Error: {e}')

def saque():
    email = input('Digite seu Email: ')
    senha = input('Digite sua senha: ')

    try:
        usuario = Usuario.get((Usuario.email == email) & (Usuario.senha == senha))


        conta = Conta.get(Conta.usuario == email)
        valor = float(input('Digite o valor do Saque: '))

        conta.saldo -= valor
        conta.save()

    except Usuario.DoesNotExist:
        print(f'Email incorreto!')
    except Exception as e:
        print(f'Error')

def status():
    email = input('Digite seu Email: ')
    senha = input('Digite sua senha: ')

    try:
        usuario = Usuario.get((Usuario.email == email) & (Usuario.senha == senha))
        conta = Conta.get(Conta.usuario == email)

        print(f'''
        Nome: {usuario.nome}
        Saldo: {conta.saldo}
        ''')

    except Usuario.DoesNotExist:
        print(f'Email incorreto!')
    except Exception as e:
        print(f'Error')

def menu():
    while(True):
        Menu = int(input('''
        1 - Cadastro
        2 - Deposito
        3 - Saque
        4 - Status
        5 - EXIT
        '''))
        if (Menu == 1):
            cadastrar_usuario()
        elif (Menu == 2):
            deposito()
        elif (Menu == 3):
            saque()
        elif (Menu == 4):
            status()
        elif (Menu == 5):
            break 
        else:
            print('Opção Incorreta!')
