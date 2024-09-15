class Usuario:
    contador_id = 1 #Realizar a contagem de id de cada usuario

    def __init__(self, nome, cpf):#Def principal para criação de nome e cpf
        self.id = Usuario.contador_id #Id do cliente
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        Usuario.contador_id += 1 #Adicionando ID

    def depositar(self, valor):
        if valor > 0: #Função para realizar o deposito caso ele n seja zero ou negativo
            self.saldo += valor
            print(f"Depósito de R${valor} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):#Função para o saque
        if 0 < valor <= self.saldo: #Verificar se tem saldo suficiente na conta
            self.saldo -= valor #Realizar a subtração no saldo
            print(f"Saque de R${valor} realizado.")
        else:
            print("Valor inválido.")

    def mostrar_saldo(self): #Função para verificando o saldo
        print(f"Saldo atual: R${self.saldo:}")


class interface:
    def __init__(self):#Lista de usuarios
        self.usuario = []

    def criar_conta(self):#Criando uma conta para o usuario
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF: ")
        conta = Usuario(nome, cpf) #Definindo o usuario a conta
        self.usuario.append(conta)
        print(f"Conta criada com sucesso! ID: {conta.id}")#Identificando a conta do usuario

    def encontrar_usuarioID(self, id_usuario):#Busca de conta pelo ID
        for conta in self.usuario:
            if conta.id == id_usuario:
                return conta
        return None

    def Funcionalidade(self): #Funcionalidade da conta
        while True:
            opcao = int(input("""Menu de Operações
0. Sair
1. Criar Conta
2. Entrar em conta
Opção: """))


            if opcao == 0:
                print("Encerrando...")
                break
            elif opcao == 1:
                self.criar_conta()
            elif opcao == 2:
                id_usuario = int(input("Digite o ID da conta: "))#Identificar em qual conta fazer
                usuario = self.encontrar_usuarioID(id_usuario)
                if usuario:
                    escolha = int(input("""Digite a função desejada:
0. Sair
1. Depositar
2. Sacar
3. Saldo em conta
Opção: """))
                    print(f"Conta de {usuario.nome}")#Nome do usuario da conta
                    if escolha == 0:
                        print("Encerrando...")
                        break
                    elif escolha == 1:
                        valor = float(input("Digite um valor para depósito: "))
                        usuario.depositar(valor)#Chama a função de deposito
                        
                    elif escolha == 2:
                        valor = float(input("Digite o valor para saque: "))
                        usuario.sacar(valor)#Função de saque
                    elif escolha == 3:
                        if usuario:
                            usuario.mostrar_saldo()#Função de saldo em conta
                    else:
                        print(f"A opção {escolha} é invalida.")
                    
                else:
                    print("Conta não encontrada.")
            else:
                    print(f"A opção {opcao} é inválida.")


# Inicializa a interface do banco
interface = interface()
interface.Funcionalidade()
