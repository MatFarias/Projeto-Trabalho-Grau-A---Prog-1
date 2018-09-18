import InserirPeca

sair = False
lista_estoque = []
lista_aux = []

while sair == False:

    print("\n1 - Inserir item\n2 - Remover peça\n3 - Sair\n")
    opcao = int(input("Selecione a opção desejada:\n"))


    if opcao == 1:

        nova_peca = InserirPeca.inserir()
        nova_peca.inserir_peca()

        lista_aux.append(nova_peca)

        if len(lista_estoque) == 0:
            lista_estoque.append(lista_aux.copy())
        else:
            for i in range(len(lista_estoque)):
                if lista_estoque[i][0] == lista_aux[0]:
                    print("Já existe um produto com o codigo {}".format(lista_aux[0]))
                    break
                else:
                    lista_estoque.append(lista_aux.copy())

        lista_aux.clear()

    if opcao == 3:
        sair = True


print(lista_estoque)




