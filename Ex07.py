# Obter o peso em kg e a altura em metros do usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcular o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibir o resultado
print(f"O Índice de Massa Corporal (IMC) é: {imc:.2f}")
