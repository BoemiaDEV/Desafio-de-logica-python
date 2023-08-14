##Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela. 

cadrasto = {"nome" : input("digite o nome: "),
            "idade" : int(input("digite sua idade: ")),
            "email" : input("digite seu email: "),
            "telefone" : int(input("digite seu numero de telefone: "))}

cadrastado = f"usuario cadrastado com sucesso {cadrasto}"

print(cadrastado)

#Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra. 

valor = ""
menu = '''
###################

digite [1] para começar a cadrastar um produto  [2] para finalizar e ver o preço: \n

######################
'''

quantidade = 0
valor = 0
while True:

    

    opcao = input(menu)

    if opcao == "1":
        codigo = input("digite o codigo do produto: \n")
        nome = input("digite o nome do podruto: \n")
        quantidade = int(input("Digite a Quantidade do produto: \n"))   
        preco = int(input("digite o preço do produto"))
        valor += preco


    elif opcao == "2":
        if valor <= 0:
            print("você ainda não cadrastrou nenhum produto")
        else:
            print(f"O valor da compra foi de {valor * quantidade} ")
    else:
        print("digite apenas 1 ou 2")
        break


#Faça um programa que converte centímetros em metros. 

cm = float(input("digite a quantidade em centimetro: "))

converter = (f"{cm}CM sao {cm * 100}M")

print(converter)

x = int("digite a base do quadrado")

soma = x * 4

print(f"A area do quadradro é {x}")