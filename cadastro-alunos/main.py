import json
from banco import carregar_alunos
from banco import salvar_alunos

alunos= carregar_alunos()

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
            buscar_alunos()
        elif escolha == "4":
            print("Vamos atualizar os dados.")
            atualizar_aluno()
        elif escolha == "5":
            print("Ok, iniciando remoção de aluno.")
            deletar_aluno()
        elif escolha == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


def cadastro():
    
    matricula= int(input("Digite o número da matrícula: "))
    nome= str(input("Digite o nome do aluno: "))
    idade= int(input("Digite a idade do aluno: "))
    curso= str(input("Digite o curso do aluno: "))
    alunos.append({'Matrícula':matricula, 'Nome':nome, 'Idade': idade, 'Curso':curso})
    print('Aluno cadastrado com sucesso!')
    salvar_alunos(alunos)



def listar_aluno():
    if not alunos:
        print("Nenhum aluno foi cadastrado.")
    else:
        for i,aluno in enumerate(alunos, start=1):
            print(f'{i}. Matrícula: {aluno['Matrícula']}, Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Curso: {aluno['Curso']}')
        print()    

def buscar_alunos():
    busca_aluno = input("Digite o nome do aluno a ser procurado: ")
    
    encontrado = False 
    
    for aluno in alunos: 
        if aluno['Nome'].lower() == busca_aluno.lower():
            print(f"Aluno encontrado: Matrícula: {aluno['Matrícula']}, Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Curso: {aluno['Curso']}")
            encontrado = True  
            break  
    
    if not encontrado:  
        print("Aluno não encontrado, é necessário fazer o cadastro.")


def atualizar_aluno():
    busca_nome=str(input("Digite o nome do aluno que desejar atualizar dados: "))

    encontrado= False

    for aluno in alunos:
        if aluno['Nome'].lower() == busca_nome.lower():
            print('Aluno encontrado, vamos para as atualizações. ')
            encontrado =True

        novo_nome=str(input("Digite o novo nome: (Enter se não for necessário atualizar) "))
        if novo_nome.strip() != "":
            aluno['Nome']= novo_nome

        nova_idade=(input("Digite a nova idade: (Enter se não for necessário atualizar)"))
        if nova_idade.strip() != "":
            aluno['Idade']= int(nova_idade)

        novo_curso=str(input("Digite o nome do novo curso: (Enter se não for necessário atualizar)"))
        if novo_curso.strip() != "":
            aluno['Curso']= novo_curso

        salvar_alunos(alunos)

        print('Dados do aluno atuaizado com sucesso.')

        break
    if not encontrado:
        print("Aluno não encontrado, é preciso fazer o cadastro.")



def deletar_aluno():
    busca_delete=(input("Digite o nome do aluno que deseja deletar: "))

    encontrado= False

    for aluno in alunos:
        if aluno['Nome'].lower() == busca_delete.lower():
            encontrado = True

            alunos.remove(aluno)
            salvar_alunos(alunos)
            
            print("O aluno esolhido já foi removido.")
            break        
    if not encontrado:
        print("Aluno não en contrado, é necessário fazer o cadastro.")


if __name__ == "__main__":
    main()    