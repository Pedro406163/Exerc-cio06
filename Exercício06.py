from collections import deque

def mostrar_menu():
    print("\n MENU FILA DE ATENDIMENTO ")
    print("1 - Adicionar pessoa à fila")
    print("2 - Atender pessoa")
    print("3 - Mostrar fila")
    print("4 - Sair")

def main():
    fila = deque()  

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome da pessoa: ").strip()
            if nome:
                fila.append(nome)
                print(f"{nome} foi adicionado(a) à fila.")
            else:
                print("Nome inválido. Tente novamente.")

        elif opcao == '2':
            if fila:
                atendido = fila.popleft()
                print(f"{atendido} foi atendido(a).")
            else:
                print("A fila está vazia. Ninguém para atender.")

        elif opcao == '3':
            if fila:
                print("\nPessoas na fila:")
                for i, pessoa in enumerate(fila, start=1):
                    print(f"{i}. {pessoa}")
            else:
                print("A fila está vazia.")

        elif opcao == '4':
            print("Encerrando o programa")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
