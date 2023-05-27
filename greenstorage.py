import re

nome_usuario_salvo = ["Guilherme", "João", "Lucas", "Pedro", "Vinícius"]
senha_sistema_salvo = "12345"

estoque = ["uva", "13/07/2023"]

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
    print("a")    

def tamanho_estoque():
    print("AAAAAAAAAAAAAAA")

def registrar_remover_produto():
    escolha = input("Certo, você deseja ADICIONAR ou REMOVER um produto?\n")
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
        if int(dia_validade) < 10:
            dia_validade = "0" + dia_validade

        mes_validade = input("\nMês: ")
        while int(mes_validade) < 1 or int(mes_validade) > 12:
            print("\nO valor inserido é inválido, verifique-o e tente novamente.")
            mes_validade = input("Mês: ")
        if int(mes_validade) < 10:
            mes_validade = "0" + mes_validade

        ano_validade = input("\nAno: ")
        while int(len(ano_validade)) !=4 or int(ano_validade) < 2023:
            print("\nO valor inserido é inválido ou está ultrapassado, verifique-o e tente novamente.")
            ano_validade = input("\nAno: ")

        data_validade = f"{dia_validade}/{mes_validade}/{ano_validade}"

        estoque.append(data_validade)
        print("\nProduto registrado no estoque com sucesso!")

    elif escolha.lower() == "remover":
        nome_produto = input("Qual é o nome do produto a ser removido do estoque?\n")
        while not nome_produto in estoque:
            print("Parece que este produto não está no estoque, verifique o nome inserido e tente novamente.")
            nome_produto = input("Digite novamente o nome do produto ou escreva SAIR para encerrar esta opção: \n")
            if nome_produto.lower() == "sair":
                break
        if not nome_produto == "sair":
            indice_produto = estoque.index(nome_produto)
            indice_validade = indice_produto + 1

            estoque.pop(indice_validade)
            estoque.pop(indice_produto)

            print(f"Produto removido do estoque com sucesso!")

print("Seja bem-vindo ao seu copiloto!")

# try:
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
# except ValueError:
#     print("Seu acesso foi bloqueado. Consulte o gerente para resolver este problema.")
