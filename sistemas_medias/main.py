alunos = []  # Aqui vamos armazenar tudo

def mostrar_menu():
    print("\n===== SISTEMA DE MÉDIAS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Relatório final")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def cadastrar_aluno():
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome do aluno: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")


def listar_alunos():
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado ainda.\n")
        return

    for aluno in alunos:
        situacao = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f} - {situacao}")
    print()


def relatorio_final():
    if not alunos:
        print("\nNenhum aluno cadastrado para gerar relatório.\n")
        return

    medias = [aluno["media"] for aluno in alunos]
    media_geral = sum(medias) / len(medias)

    print("\n===== RELATÓRIO FINAL =====")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Total de alunos: {len(alunos)}")

    aprovados = len([a for a in alunos if a["media"] >= 7])
    reprovados = len([a for a in alunos if a["media"] < 7])

    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}\n")


def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            relatorio_final()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
