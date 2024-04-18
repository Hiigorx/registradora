#Calculadora de Notas

#qtdNotas = int(input("Digite a quantidade de notas desejadas: "))
#soma = 0
#contador = 0
#
#while qtdNotas > 0:
#    notas = int(input("Digite a nota: "))
#    contador = contador + 1
#    soma = soma + notas
#    qtdNotas = qtdNotas - 1
#
#media = soma / contador
#print(f'A média das notas é de: {media}')





#media = 0
#soma = 0
#contador = 0
#
#while True:
#
#    selecao = int(input("Digite um número inteiro: "))
#    if selecao == 0:
#        break
#    contador = contador + 1
#    soma = soma + selecao
#    media = soma / contador
#
#print(f'A soma dos valores digitados é de: {soma:.2f}\nA média aritmética dos números digitados é de: {media:.2f}')
#print("Fim da execução.")



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
    else:
        print("Codigo invalido.")
        break



    if pedido == 0:
        soma = (produto1 * qtd1) + (produto2 * qtd2) + (produto3 * qtd3) + (produto5 * qtd5) + (produto9 * qtd9)
        break
        print(soma)
