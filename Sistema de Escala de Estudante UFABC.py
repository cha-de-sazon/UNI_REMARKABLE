alunos = []

semana = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]

# Função menu, responsável por mostrar e disponibilizar acesso às funções do sistema
def menu():
    opcoes = [["Registrar Perfil", registrar], ["Acessar Perfil", acessar], ["Excluir Perfil", excluir]]

    print("Digite o número correspondente para selecionar a opção")
    for i in opcoes:
        print(f"[{opcoes.index(i)+1}] {opcoes[opcoes.index(i)][0]}")
    comando = int(input("Selecione: "))
    return opcoes[comando - 1][1]()

# Função responsável por criar a matriz de dados dos alunos, indexa informações de maneira eficiente para criar matrizes melhor operáveis
def registrar():
    nome = str(input("Nome do aluno: "))
    materias = []

    nascimento = str(input("Dia de nascimento: ")+"/"+input("Mês de Nascimento (Número): ")+"/"+input("Ano de nascimento: "))
    curso = str(input("Curso: "))
    quad = int(input("Quadrimestre atual: "))
    for i in range(int(input("Número de matérias matriculadas: "))):
        materias.append([str(input(f"{i+1}ª Matéria: "))])
    for i in materias:
        for l in range(2):
            materias[materias.index(i)].append([str(f"Quinzenal {l+1}")])
            print(f"Quinzenal {l+1}")
            for k in range(int(input(f"Quantos dias da semana você tem aula de {i[0]} no Quinzenal {l+1}? "))):
                print(f"Selecione o {k+1}º dia de aula de {i[0]} da semana do Quinzenal {l+1} digitando o valor '[n]' correspondente")
                for j in range(7):
                    print(f"[{j+1}] {semana[j]}")
                materias[materias.index(i)][l+1].append([semana[int(input("Selecione: "))-1], str(input(f"Horário da aula (hh:mm): "))])
    alunos.append([nome, nascimento, curso, quad, materias])
    input("Dados Cadastrados. Aperte Enter para continuar")
    menu()
# Formatação matriz de dados: [nome, nascimento, curso, [materia, [Q1, [dia, horario], [dia, horario]], [Q2, [dia, horario], [dia, horario]]]]


# Função responsável por mostrar os perfis cadastrados e encaminhar o usuário
def acessar():
    print("Digite o número do perfil para abrir")
    for i in alunos:
        print(f"[{alunos.index(i)+1}] {i[0]}")
    perfil = alunos[int(input("Selecione: "))-1]
    print(f"Nome: {perfil[0]}")
    print(f"Data de Nascimento: {perfil[1]}")
    print(f"Curso: {perfil[2]}, {perfil[3]}º quadrimestre")
    print("Turmas - ")
    for i in perfil[4]:
        print(i[0])
        print(i[1])
        print(i[2])
        print("")
    input("Aperte Enter para retornar ao menu")
    menu()


# Função para excluir perfis
def excluir():
    print("Digite o número do perfil para excluir")
    for i in alunos:
        print(f"[{alunos.index(i)+1}] {i[0]}")
    perfil = alunos[int(input("Selecione: "))-1]
    alunos.remove(perfil)
    menu()

menu()
