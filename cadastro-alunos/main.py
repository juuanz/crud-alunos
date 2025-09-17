def exibir_menu():
    print("----------- Sistema de Cadastro de Alunos -----------")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno pelo nome")
    print("4 - Atualizar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número da ação desejada: ")

        if escolha == "1":
            print("Ok, vamos para o cadastro! ")
            cadastro()
        elif escolha == "2":
            print("===Lista de Alunos===")
            listar_aluno()
        elif escolha == "3":
            print("Iniciando a busca por nome\n")
            buscar_aluno()
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

alunos=[]
def cadastro():
    
    matricula= int(input("Digite o número da matrícula: ")),
    nome= str(input("Digite o nome do aluno: ")),
    idade= int(input("Digite a idade do aluno: ")),
    curso= str(input("Digite o curso do aluno: ")),
    alunos.append({'Matrícula':matricula, 'Nome':nome, 'Idade': idade, 'Curso':curso})
    print('Aluno cadastrado com sucesso!')



if __name__ == "__main__":
    main()    

def listar_aluno():
    if not alunos:
        print("Nenhum aluno foi cadastrado.")
    else:
        for i,aluno in enumerate(alunos, start=1):
            print(f'{i}. Matrícula: {alunos['matricula']}, Nome: {alunos['nome']}, Idade: {alunos['idade']}, Curso: {alunos['curso']}')
        print()    

def buscar_aluno():
    busca_aluno=str(input("Digite o nome do aluno a ser procurado: "))
    
    encontrado=False
    if not busca_aluno in alunos:
        print("Aluno não encontrado, é necessário fazer o cadastro.")
    for aluno in alunos:
        if aluno.lower() == busca_aluno():
            print(f'Aluno encontrado: Matrícula: {alunos["matricula"]}, Nome: {alunos["nome"]}, Idade: {alunos["idade"]}, Curso: {alunos["curso"]}')
            break

