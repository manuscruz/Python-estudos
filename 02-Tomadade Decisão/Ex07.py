# Solicitar a idade ao usuário
idade = int(input("Digite sua idade: "))

# Identificar a faixa etária
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
