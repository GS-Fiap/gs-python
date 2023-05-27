nome_usuario_salvo = ["Guilherme", "João", "Lucas", "Pedro", "Vinícius"]
senha_sistema_salvo = "12345"


print("Seja bem-vindo ao seu copiloto!")

try:
    for i in range(1, 4, 1):
        print(i)
        nome_usuario = input("Digite o seu nome: ")
        senha_sistema = input("Digite a senha do sistema: ")

        if i == 3 and not (nome_usuario in nome_usuario_salvo and senha_sistema == senha_sistema_salvo):
            raise ValueError
        else: 
            if not (nome_usuario in nome_usuario_salvo and senha_sistema == senha_sistema_salvo):
                print("Seu nome ou a senha do sistema está incorreto. Tente novamente.")
            else:
                break


    print(f"Olá, {nome_usuario}. Como posso ajudá-lo?")
    print("\n1-Quero fazer uma previsão de demanda\n2-Quero acessar a validade dos meus produtos\n3-Quero saber o tamanho do meu estoque")
    escolha = int(input())
    if escolha == 1:
        print("A")
    elif escolha == 2:
        print("B")
    elif escolha == 3:
        print("C")
    else:
        print("Você selecionou uma opção inexistente.")

except ValueError:
    print("Seu acesso foi bloqueado. Consulte o gerente para resolver este problema.")
