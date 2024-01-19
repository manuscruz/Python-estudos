# Solicitar login e senha ao usuário
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar o login e senha
if login == "admin" and senha == "admin123":
    print("Acesso permitido! Bem-vindo, admin.")
else:
    print("Login ou senha incorretos. Acesso negado.")
