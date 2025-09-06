SENHA = input("Qual é a senha?")
SenhaCorreta = "WSXDRFVGYHNJIK"

def senhaAlt(Senha_Digitada):
    if Senha_Digitada == SenhaCorreta:
        print(f"Entrada Permitida, {Senha_Digitada}")
    else:
        print("Senha Incorreta!")
senhaAlt(SENHA)
