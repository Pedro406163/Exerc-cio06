from collections import deque

def mostrar_menu():
    print("\n FILA DA MONTANHA-RUSSA")
    print("1 - Entrar na fila")
    print("2 - Embarcar pessoa")
    print("3 - Mostrar fila")
    print("4 - Encerrar o sistema")

def main():
    fila = deque()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do visitante: ").strip()
            if nome:
                fila.append(nome)
                print(f"{nome} entrou na fila da montanha-russa!")
            else:
                print("Nome inválido. Tente novamente.")

        elif opcao == '2':
            if fila:
                embarcado = fila.popleft()
                print(f"{embarcado} embarcou na montanha-russa!")
            else:
                print("Nenhum visitante na fila no momento.")

        elif opcao == '3':
            if fila:
                print("\n Visitantes na fila:")
                for i, pessoa in enumerate(fila, start=1):
                    print(f"{i}. {pessoa}")
            else:
                print("A fila está vazia. Ninguém esperando para embarcar.")

        elif opcao == '4':
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()
