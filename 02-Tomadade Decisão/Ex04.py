# Solicitar uma nota ao usuário
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verificar e classificar o aluno
if 0 <= nota <= 10:
    if nota >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")
else:
    print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
