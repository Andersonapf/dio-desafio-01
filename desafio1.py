menu = """\n
================ MENU ================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

======================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite o valor para deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")   

    elif opcao == "s":
        numnero_saque += 1
        valor = float(input("Informe o valor de saque: "))

        exedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite permitido de R$500,00")

        elif excedeu_saques:
            print("Operação falhou! Limite de saque já atingindo")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação invalida! O valor informado é invalido")



    elif opcao == "e":
        print("\n================= EXTRATO ================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        break    

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")       
