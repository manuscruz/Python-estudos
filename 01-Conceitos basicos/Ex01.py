# Função para realizar a soma
def soma(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    # Adicionando um tratamento de divisão por zero
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

# Solicitar os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizar as operações
resultado_soma = soma(numero1, numero2)
resultado_subtracao = subtracao(numero1, numero2)
resultado_multiplicacao = multiplicacao(numero1, numero2)
resultado_divisao = divisao(numero1, numero2)

# Exibir os resultados
print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")
print(f"Multiplicação: {resultado_multiplicacao}")
print(f"Divisão: {resultado_divisao}")