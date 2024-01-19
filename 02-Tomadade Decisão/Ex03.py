while True:
    # Solicitar uma nota ao usuário
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    # Verificar se a nota é válida
    if 0 <= nota <= 10:
        print(f"Você inseriu a nota: {nota}")
        break  # Sai do loop se a nota for válida
    else:
        print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
