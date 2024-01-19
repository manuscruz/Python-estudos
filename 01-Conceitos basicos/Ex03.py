# Obter a quantidade de quilômetros do usuário
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Fator de conversão
metros_por_quilometro = 1000
centimetros_por_quilometro = 100000
milimetros_por_quilometro = 1000000

# Converter para metros, centímetros e milímetros
metros = quilometros * metros_por_quilometro
centimetros = quilometros * centimetros_por_quilometro
milimetros = quilometros * milimetros_por_quilometro

# Exibir os resultados
print(f"{quilometros} quilômetros é igual a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
