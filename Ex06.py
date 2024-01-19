# Velocidades em km/h
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Distância do percurso em km (você pode ajustar conforme necessário)
distancia_percurso = float(input("Digite a distância do percurso em quilômetros: "))

# Calcular o tempo de viagem para cada meio de transporte
tempo_aviao = distancia_percurso / velocidade_aviao
tempo_carro = distancia_percurso / velocidade_carro
tempo_onibus = distancia_percurso / velocidade_onibus

# Exibir os resultados
print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")