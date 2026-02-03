def ler_inteiro():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            return num
        except:
            print("Isso não é um número inteiro. Tente novamente.")


def adicionar_numeros(lista):
    while True:
        num = ler_inteiro()

        if num == 0:
            break

        lista.append(num)


def remover_numero(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
        return

    remove = ler_inteiro()

    if remove in lista:
        lista.remove(remove)
        print("Número removido com sucesso!")
    else:
        print("Esse número não está na lista.")


def procurar_numero(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
        return

    procurar = ler_inteiro()

    if procurar in lista:
        print("O número", procurar, "está na lista.")
    else:
        print("O número", procurar, "não está na lista.")


def crescente_decrescente(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
        return

    print("Como deseja ordenar a lista?")
    ordem = ler_inteiro()

    if ordem == 1:
        lista.sort()
        print("Números ordenados (crescente):")
        print(lista)

    elif ordem == 2:
        lista.sort(reverse=True)
        print("Números ordenados (decrescente):")
        print(lista)

    else:
        print("Opção inválida.")


def calcular_soma_media(lista):
    if len(lista) == 0:
        return 0, 0

    soma = 0
    for num in lista:
        soma += num

    media = soma / len(lista)
    return soma, media


def encontrar_maior_menor(lista):
    if len(lista) == 0:
        return None, None

    maior = lista[0]
    menor = lista[0]

    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    return maior, menor


def separar_pares_impares(lista):
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares


def salvar_dados(lista):
    with open("dados.txt", "w", encoding="utf-8") as arquivo:
        for num in lista:
            arquivo.write(str(num) + "\n")

    print("Dados salvos com sucesso!")


def carregar_dados():
    lista = []

    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                lista.append(int(linha.strip()))

        print("Dados carregados com sucesso!")

    except:
        print("Nenhum arquivo encontrado. Começando com lista vazia.")

    return lista


# ---------------- PROGRAMA PRINCIPAL ----------------

numeros = []

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar números")
    print("2 - Mostrar relatório")
    print("3 - Limpar a lista")
    print("4 - Remover número da lista")
    print("5 - Procurar número na lista")
    print("6 - Ordenar lista")
    print("7 - Salvar dados")
    print("8 - Carregar dados")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_numeros(numeros)

    elif opcao == "2":
        soma, media = calcular_soma_media(numeros)
        maior, menor = encontrar_maior_menor(numeros)
        pares, impares = separar_pares_impares(numeros)

        print("\n--- RELATÓRIO ---")
        print("Números:", numeros)
        print("Soma:", soma)
        print("Média:", media)
        print("Maior:", maior)
        print("Menor:", menor)
        print("Pares:", pares)
        print("Ímpares:", impares)
        print("Quantidade de números:", len(numeros))
        print("Quantidade de pares:", len(pares))
        print("Quantidade de ímpares:", len(impares))

    elif opcao == "3":
        print("Limpando a lista.")
        numeros.clear()

    elif opcao == "4":
        remover_numero(numeros)

    elif opcao == "5":
        procurar_numero(numeros)

    elif opcao == "6":
        crescente_decrescente(numeros)

    elif opcao == "7":
        salvar_dados(numeros)

    elif opcao == "8":
        numeros = carregar_dados()

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
