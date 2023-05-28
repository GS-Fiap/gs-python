import re

nome_usuario_salvo = ["Guilherme", "João", "Lucas", "Pedro", "Vinícius"]
senha_sistema_salvo = "12345"

estoque = ["Uva", "13/07/2023", "125", "Suco de Laranja", "04/05/2023", "32", "Limão Verde", "31/12/2023", "204"]

continuar = "sim"

def previsao_demanda():
    somatoria = 0
    nome_produto = input("\nMuito bem. Insira o nome do produto que deseja realizar este estudo:")
    print("\nAgora, preciso que você insira a quantidade de meses que você deseja considerar e as vendas deste produto para cada um desses meses.")
    tempo_meses = int(input("\nDigite quantos meses devem ser considerados: "))
    print("\nInsira abaixo a quantidade de vendas para cada mês:\n")
    for i in range(1, tempo_meses+1, 1):
        num_vendas = int(input(f"{i}° Mês: "))
        somatoria += num_vendas
    media = somatoria / tempo_meses
    print(f"\nTendo em vista a quantidade de vendas nos últimos {tempo_meses} meses, espera-se que no próximo mês a demanda para {nome_produto} será de {media:.1f} unidades.")

def validade_produtos():
    escolha = input("\nVocê deseja acessar a validade de um produto ESPECÍFICO ou de TODOS que estão no estoque?\n")
    while (escolha.lower() != "específico" and escolha.lower() != "especifico") and escolha.lower() != "todos":
        escolha = input("Desculpe, não entendi a sua resposta. Você deseja acessar a validade de um produto ESPECÍFICO ou de TODOS que estão no estoque?\n")

    if escolha.lower() == "todos":
        print("\nCerto, segue abaixo a lista dos seus produtos com a respectiva data de validade:\n")
        for i in range(0, len(estoque), 2):
            print(f"Nome do Produto: {estoque[i]}")
            print(f"Data de validade: {estoque[i+1]}\n")
    elif escolha.lower() == "específico" or escolha.lower() == "especifico":
        nome_produto = input("\nE qual é o nome do produto que você deseja consultar?\n")

        for i in range(len(estoque)):
                if nome_produto == estoque[i]:
                    print(f"\nA data de validade do produto escolhido é esta: {estoque[i+1]}.")
                    break

def tamanho_estoque():
    quantidade = 0
    escolha = input("\nMas você quer saber o tamanho do estoque INTEIRO ou de um produto ESPECÍFICO?\n")
    while (escolha.lower() != "específico" and escolha.lower() != "especifico") and escolha.lower() != "inteiro":
        escolha = input("Desculpe, não entendi a sua resposta. Você quer saber o tamanho do estoque INTEIRO ou de um produto ESPECÍFICO?\n")

    if escolha.lower() == "inteiro":
        for i in range(2, len(estoque), 3):
            quantidade += int(estoque[i])

        print(f"O tamanho do seu estoque inteiro é de {quantidade} itens.")

    elif escolha.lower() == "específico" or escolha.lower() == "especifico":
        nome_produto = input("\nE qual é o nome do produto que você deseja consultar?\n")

        for i in range(len(estoque)):
                if nome_produto == estoque[i]:
                    print(f"\nEste produto possui {estoque[i+2]} itens.")
                    break

def registrar_remover_produto():
    escolha = input("\nCerto, você deseja ADICIONAR ou REMOVER um produto?\n")
    while  not escolha.lower() == "adicionar" and not escolha.lower() == "remover":
        print("Desculpe, mas não entendi a sua resposta. Você deseja ADICIONAR ou REMOVER um produto?")
        escolha = input()
    if escolha.lower() == "adicionar":
        nome_produto = input("\nQual é nome do produto a ser adicionado?\n")
        estoque.append(nome_produto)
        print("\nE qual é a data de validade deste produto?")
        dia_validade = input("\nDia: ")
        while int(dia_validade) < 1 or int(dia_validade) > 31:
            print("\nO valor inserido é inválido, verifique-o e tente novamente.")
            dia_validade = input("\nDia: ")
        if dia_validade[0] != "0":
            dia_validade = "0" + dia_validade

        mes_validade = input("\nMês: ")
        while int(mes_validade) < 1 or int(mes_validade) > 12:
            print("\nO valor inserido é inválido, verifique-o e tente novamente.")
            mes_validade = input("Mês: ")
        if mes_validade[0] != "0":
            mes_validade = "0" + mes_validade

        ano_validade = input("\nAno: ")
        while int(len(ano_validade)) !=4 or int(ano_validade) < 2023:
            print("\nO valor inserido é inválido ou está ultrapassado, verifique-o e tente novamente.")
            ano_validade = input("\nAno: ")

        data_validade = f"{dia_validade}/{mes_validade}/{ano_validade}"

        estoque.append(data_validade)

        print("\nQuantos itens você quer registrar para este produto?\n")
        quantidade_itens = input("")
        estoque.append(quantidade_itens)

        print("\nProduto registrado no estoque com sucesso!")
        print(estoque)

    elif escolha.lower() == "remover":
        nome_produto = input("Qual é o nome do produto a ser removido do estoque?\n")
        while not nome_produto in estoque:
            print("Parece que este produto não está no estoque, verifique o nome inserido e tente novamente.")
            nome_produto = input("Digite novamente o nome do produto ou escreva SAIR para encerrar esta opção: \n")
            if nome_produto.lower() == "sair":
                break
        if not nome_produto == "sair":
            for i in range(len(estoque)):
                if nome_produto == estoque[i]:
                    estoque.pop(i+2)
                    estoque.pop(i+1)
                    estoque.pop(i)
                    break

            print(f"Produto removido do estoque com sucesso!")

print("Seja bem-vindo ao seu assistente!")

try:
    for i in range(1, 4, 1):
        nome_usuario = input("Digite o seu nome: ")
        senha_sistema = input("Digite a senha do sistema: ")

        if i == 3 and not (nome_usuario in nome_usuario_salvo and senha_sistema == senha_sistema_salvo):
            raise ValueError
        else: 
            if not (nome_usuario in nome_usuario_salvo and senha_sistema == senha_sistema_salvo):
                print("Seu nome ou a senha do sistema está incorreto. Tente novamente.")
            else:
                break


    print(f"\nOlá, {nome_usuario}.")
    while continuar == "sim":
        print("\nComo posso ajudá-lo?")
        print("\n1-Quero fazer uma previsão de demanda\n2-Quero acessar a validade dos meus produtos\n3-Quero saber o tamanho do meu estoque\n4-Quero registrar um novo produto ou remover um produto do estoque\n")
        escolha = int(input())

        while not (escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4):
            print("Você selecionou uma opção inexistente. Tente de novo.")
            escolha = int(input())

        if escolha == 1:
            continuar = "não"
            previsao_demanda()
        elif escolha == 2:
            if estoque == []:
                print("\nParece que você não tem nenhum produto registrado no estoque, tente fazer isto antes de acessar esta opção.")
                continue
            else:
                continuar = "não"
                validade_produtos()
        elif escolha == 3:
            continuar = "não"
            tamanho_estoque()
        elif escolha == 4:
            continuar = "não"
            registrar_remover_produto()

        continuar = input("\nEspero ter ajudado. Você deseja o meu auxílio em mais alguma coisa? (Sim/Não)\n")

    print("Certo, volte quando quiser!")
except ValueError:
    print("Seu acesso foi bloqueado. Consulte o gerente para resolver este problema.")
