# Obter o número de horas de exercício físico por semana do usuário
horas_por_semana = float(input("Digite o número de horas de exercício físico por semana: "))

# Calcular o total de minutos de exercício por semana e por mês
minutos_por_semana = horas_por_semana * 60
minutos_por_mes = minutos_por_semana * 4  # assumindo um mês de 4 semanas

# Calcular o total de calorias queimadas
calorias_por_minuto = 5
total_calorias = minutos_por_mes * calorias_por_minuto

# Exibir o resultado
print(f"Você queimou um total de {total_calorias} calorias em um mês de exercício físico.")
