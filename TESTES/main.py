contador = 0
while():
    try:
        nomeCompleto = str(input("Nome Completo: "))
        anoNascimento = int(input("Ano nascimento: "))
        idade = 2022 - anoNascimento

        if (anoNascimento < 1921):
            print("Idade inválida")
        else:
            print("-"*40)
            print("Sua idade")
            print("Nome Completo:", nomeCompleto)
            print( "Idade:", idade)
    except:
        print("Você não digitou os dados corretamente.")