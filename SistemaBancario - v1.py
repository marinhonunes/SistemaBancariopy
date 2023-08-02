saldo = (0) 
limite_saques = 3
saques_realizados = 0
extrato = ""  
saque_maximo = 500

while True:
    opcao = input(""" 
          Seja bem vindo!
    Selecione a opção desejada:
        
        (d) depositar
        (s) sacar 
        (e) extrato
        (q) sair
                  
        """)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += (f"\nDepósito de: R${valor:.2f}")
            print("Depósito realizado com sucesso!.")
        else:
            print("Operação inválida! Informe um valor maior que 0.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        falta_saldo = valor > saldo

        limite = saques_realizados >= limite_saques

        saque_superior = valor > saque_maximo

        if saque_superior:
            print("O saque não pode ser superior a R$ 500,00")

        elif limite:
            print("Operação falhou! O total de saques diários não pode ser superior a 3.")

        elif falta_saldo:
            ("Saque indisponível por falta de saldo.")
        
        elif valor > 0:
            print(f"Operação realizada com sucesso! Saque de {valor:.2f}")
            saldo -= valor
            saques_realizados +=1
            extrato += (f"\nSaque de: R${valor:.2f}")
        
        else:
            ("Operação falhou, informe dados validos.")
    
    elif opcao == ("e"):
        print(f""" 
              Extrato da conta
              {extrato}
              
              Saldo Atual: {saldo}  
              """)
    elif opcao == ("q"):
        break
    else:
        ("Operação inválida, selecione a opção desejada.")

print("Operação Finalizada!")