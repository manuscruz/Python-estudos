# Solicitar os comprimentos dos lados do triângulo ao usuário
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verificar e classificar o triângulo
if lado1 == lado2 == lado3:
    print("O triângulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")
