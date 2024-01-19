# Obter a quantidade de litros de combustível consumidos e a distância percorrida
litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))
distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

# Calcular o consumo médio em km/l
consumo_medio = distancia_percorrida / litros_consumidos

# Exibir o resultado
print(f"O consumo médio é de {consumo_medio:.2f} km/l")