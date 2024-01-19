# Obter o salário bruto e o percentual de desconto do Imposto de Renda
salario_bruto = float(input("Digite o salário bruto: "))

# Calcular o desconto do Imposto de Renda
if salario_bruto <= 1903.98:
    desconto_ir = 0
elif salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
elif salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
elif salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
else:
    desconto_ir = salario_bruto * 0.275

# Calcular o salário líquido
salario_liquido = salario_bruto - desconto_ir
# Exibir os resultados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda: R${desconto_ir:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
