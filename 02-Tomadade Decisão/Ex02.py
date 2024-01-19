# Solicitar o turno de estudo ao usuário
turno_estudo = input("Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

# Verificar o turno e imprimir a mensagem correspondente
if turno_estudo.upper() == 'M':
    print("Bom Dia!")
elif turno_estudo.upper() == 'V':
    print("Boa Tarde!")
elif turno_estudo.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
