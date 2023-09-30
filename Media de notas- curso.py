def ler_nome_aluno():
    nome = input('Digite o nome do aluno(a): ')
    return nome

def ler_notas():
    try:
        nota = float(input('Digite a nota do aluno(a): '))
        return nota
    except ValueError:
        print('Por favor, insira um valor numérico válido para a nota.')
        return ler_notas()  # Chama recursivamente a função se a entrada for inválida

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def resultado(nome, n1, n2):
    media = calcular_media(n1, n2)
    print("\nNome do aluno: ", nome)
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média:", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

# Solicita o nome do aluno
nome_aluno = ler_nome_aluno()

# Solicita as duas notas do aluno
print("\nDigite a primeira nota do aluno.")
nota1 = ler_notas()
print("\nDigite a segunda nota do aluno.")
nota2 = ler_notas()

# Calcula e exibe o resultado
resultado(nome_aluno, nota1, nota2)

