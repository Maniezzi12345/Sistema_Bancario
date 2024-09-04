# Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
# Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato

# Operação de saque

# O sistema deve permitir realizar :
# $ 3 saques diários com limite máximo de R$ 500,00 por saque. ok
# $ Caso o usuário não tenha saldo em conta, exibir uma mensagem informando não será possível sacar o dinheiro por falta de saldo.
# $ Todos os saques devem ser armazenados em uma  variável e exibidos na operação de extrato.

# Operação de depósito

# $ Deve ser possível depositar valores positivos para a minha conta bancária.
# $ A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar 
# em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser 
# armazenados em uma variável e exibidos na operação de extrato.
from datetime import datetime


data_hora_atual = datetime.now()
conta = 500
NUMERO_SAQUES = 3
deposito = 0
valores_depositados = []
valores_sacados = []

while True:
    menu = int(input("""Digite a operação desejada:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
                    
    => """))
    print(menu)

    if menu == 1:
        while deposito >= 0:
            dinheiro_depositar = int(input("Digite um valor para depósito: "))
            if dinheiro_depositar < 0:
                print("Não é possível depositar esse valor. Digite outro valor válido:")

            else:
                valores_depositados.append(dinheiro_depositar)
                conta += dinheiro_depositar
                print(f"""Saldo total da conta: R${conta:.2f}
Dinheiro depositado!""")
                print("_______________________________________________________________________________")
                finalizar_deposito = int(input("Para finalizar a operação de depósito, digite [4] ou continue [1]: "))
               
                if finalizar_deposito == 4:
                    print("Operação de depósito finalizada!")
                    break

                elif finalizar_deposito == 1:
                    continue

                else:
                    break
                
    elif menu == 2:
        while NUMERO_SAQUES > 0:
            saque = int(input("Qual valor deseja sacar? "))
            if saque > 500 or saque < 5:
                print("Não é possível realizar saques acima de R$500,00 ou inferiores a R$5,00!")
                print(f"Saldo disponível na conta: R${conta:.2f}")
                print("_______________________________________________________________________________")

            else:
                if conta <= 0:
                    print("Não há saldo suficiente para realizar o saque!")
                    print(f"Saldo disponível na conta: R${conta:.2f}")
                    print("Operação finalizada!")
                    print("_______________________________________________________________________________")
                    break

                else:
                    valores_sacados.append(saque)
                    print("Saque liberado")
                    print("_______________________________________________________________________________")
                    NUMERO_SAQUES -= 1
                    conta -= saque

        print("Você excedeu o limite de saques diários!")
        print(f"Saldo disponível: R${conta:.2f}")

    elif menu == 3:
        print("""------- EXTRATO ---------
Valores depositados:""")       
        for valores in valores_depositados:
         print(f"R${valores}.00")
        
        print("Valores sacados:")
        for valor in valores_sacados:
            print(f"R${valor}.00")


        
        print(data_hora_atual)
        print("--------------------------")

    elif menu == 4:
        print("Operação finalizada!")
        break

    else:
        print("Número inválido, tente novamente!")
