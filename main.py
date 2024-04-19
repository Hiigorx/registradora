produto1 = 0
produto2 = 0
produto3 = 0
produto5 = 0
produto9 = 0


qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd5 = 0
qtd9 = 0
cod1 = 0.50
cod2 = 1.00
cod3 = 4.00
cod5 = 7.00
cod9 = 8.00


pgt1 = "DÉBITO"
pgt2 = "CRÉDITO"
pgt3 = "PIX"
pgt4 = "BOLETO BANCÁRIO"

print('''Código -------- Preço 
   1   --------  0,50
   2   --------  1,00
   3   --------  4,00
   5   --------  7,00
   9   --------  8,00 ''')
while True:
    pedido = int(input("Digite o código do produto desejado: "))
    if pedido == 1:
        produto1 = cod1
        qtd1 = int(input("Digite a quantidade desejada do produto selecionado: "))
    elif pedido == 2:
        produto2 = cod2
        qtd2 = int(input("Digite a quantidade desejada do produto selecionado: "))
    elif pedido == 3:
        produto3 = cod3
        qtd3 = int(input("Digite a quantidade desejada do produto selecionado: "))
    elif pedido == 5:
        produto5 = cod5
        qtd5 = int(input("Digite a quantidade desejada do produto selecionado: "))
    elif pedido == 9:
        produto9 = cod9
        qtd9 = int(input("Digite a quantidade desejada do produto selecionado: "))
    elif pedido == 0:
        soma = (produto1 * qtd1) + (produto2 * qtd2) + (produto3 * qtd3) + (produto5 * qtd5) + (produto9 * qtd9)
        print(f"O valor da sua compra foi de R${soma}.")
        pgt = int(input('''---------- FORMAS DE PAGAMENTO ACEITAS ----------
        [1] DÉBITO
        [2] CRÉDITO
        [3] PIX
        [4] BOLETO BANCÁRIO
        
        DEFINA A FORMA DE PAGAMENTO UTILIZADA: '''))

        if pgt == 1:
            print(f"Você selecionou {pgt1} como forma de pagamento para a sua compra de R${soma}.")
            conclusao = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))

            test = 1,2
            if conclusao == 1:
                print("Obrigado pela sua compra, até a próxima!")
                break
            elif conclusao == 2:
                continue
            while conclusao !=  test:
                final = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))
                if final == 1:
                    print("Obrigado pela sua compra, até a próxima!")
                    break

                else:
                    continue
        elif pgt == 2:
            print(f"Você selecionou {pgt2} como forma de pagamento para a sua compra de R${soma}.")
            conclusao = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))

            test = 1,2
            if conclusao == 1:
                print("Obrigado pela sua compra, até a próxima!")
                break
            elif conclusao == 2:
                continue
            while conclusao !=  test:
                final = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))
                if final == 1:
                    print("Obrigado pela sua compra, até a próxima!")
                    break

                else:
                    continue
        elif pgt == 3:
            print(f"Você selecionou {pgt3} como forma de pagamento para a sua compra de R${soma}.")
            conclusao = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))

            test = 1,2
            if conclusao == 1:
                print("Obrigado pela sua compra, até a próxima!")
                break
            elif conclusao == 2:
                continue
            while conclusao !=  test:
                final = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))
                if final == 1:
                    print("Obrigado pela sua compra, até a próxima!")
                    break

                else:
                    continue
        elif pgt == 4:
            print(f"Você selecionou {pgt4} como forma de pagamento para a sua compra de R${soma}.")
            conclusao = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))

            test = 1, 2
            if conclusao == 1:
                print("Obrigado pela sua compra, até a próxima!")
                break
            elif conclusao == 2:
                continue
            while conclusao != 1 or conclusao != 2:
                conclusao = int(input('''Você deseja encerrar a sua compra?
            [1] SIM
            [2] NÃO
            '''))
                if conclusao == 1:
                    print("Obrigado pela sua compra, até a próxima!")
                    break

                else:
                    continue

    else:
        print("Codigo invalido.")
        continue




