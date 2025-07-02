menu = """

[d] Depositar
[s] Sacar
[e] Extratp
[q] Sair

==> """

saldo =  0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Opção inválida. Verifique o valor do saque.")

        elif excedeu_limite:
            print("Opção inválida. Verifique o seu limite de saque.")

        elif excedeu_saques:
            print("Opção inválida. Verifique o número de saques realizados.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Saque inválido ou limite de saques atingido.")

    elif opcao == "e":
        print("=== Extrato ===")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        print("Saindo do sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")