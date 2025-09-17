def exibir_menu():
    print("----------- Sistema de Cadastro de Alunos -----------")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno por matrícula")
    print("4 - Atualizar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número da ação desejada: ")

        if escolha == "1":
            print("Cadastro de aluno ainda não implementado.")
        elif escolha == "2":
            print("Listagem de alunos ainda não implementada.")
        elif escolha == "3":
            print("Busca ainda não implementada.")
        elif escolha == "4":
            print("Atualização ainda não implementada.")
        elif escolha == "5":
            print("Remoção ainda não implementada.")
        elif escolha == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
