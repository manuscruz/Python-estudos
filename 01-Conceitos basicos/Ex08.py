# Obter o valor ganho por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_no_mes = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcular o salário total
salario_total = valor_por_hora * horas_trabalhadas_no_mes

# Exibir o resultado
print(f"Seu salário total no mês é: R${salario_total:.2f}")
