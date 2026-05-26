import os
opcao = 0
pessoa_nome = []
pessoa_email = []
pessoa_telefone = []

while opcao != 5:
    print("-------------- MENU DE CADASTRO --------------")
    print("1 - Cadastrar dados")
    print("2 - Listar usuários")
    print("3 - Alterar dados")
    print("4 - Excluir dados")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
 
    if (opcao == 1):
        nome = input("Insira seu nome: ")
        pessoa_nome.append(nome)
 
        email = input("Insira seu email: ")
        pessoa_email.append(email)
 
        telefone = input("Insira seu telefone: ")
        pessoa_telefone.append(telefone)

        print("Seus dados foram cadastrados com sucesso!")
        input()
        os.system("cls")
        
   
    if opcao == 2:
        for name, gmail, tele in zip (pessoa_nome, pessoa_email, pessoa_telefone):
            print("___________________________________________________________\n")
            print (f"Nome: {name} | E-mail: {gmail} | Telefone: {tele}")


            input()
            os.system("cls")

    elif opcao == 3:
        print("O que você quer alterar?:")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Telefone")
        escolha = int(input("Digite a opção desejada: "))

        if escolha == 1:
            print("--------------------------------------------------------") 
            mudanca1 = int(input("Qual nome deseja mudar?: "))
            novo_nome = str(input("Mude o nome: "))
            pessoa_nome[mudanca1] = novo_nome

        elif escolha == 2:
            print("--------------------------------------------------------")
            mudanca2 = int(input("Qual email deseja mudar?: "))
            novo_email = str(input("Mude o email: "))
            pessoa_email[mudanca2] = novo_email

        elif escolha == 3:
            print("--------------------------------------------------------")
            mudanca3 = int(input("Qual telefone deseja mudar?: "))
            novo_tele = int(input("Mude o telefone: "))
            pessoa_telefone[mudanca3] = novo_tele
    
        input()
        os.system("cls")
    
    elif opcao == 4:
        print("O que você quer excluir?:")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Telefone")
        decisao = int(input("Digite a opção desejada: "))

        if decisao == 1:
            print("--------------------------------------------------------")
            exclusao1 = int(input("Qual nome deseja tirar?: "))
            pessoa_nome.pop() == exclusao1
        if decisao == 2:
            print("--------------------------------------------------------")
            exclusao2 = int(input("Qual email deseja tirar?: "))
            pessoa_email.pop() == exclusao2
        if decisao == 1:
            print("--------------------------------------------------------")
            exclusao3 = int(input("Qual telefone deseja tirar?: "))
            pessoa_telefone.pop() == exclusao3

        input()
        os.system("cls")

