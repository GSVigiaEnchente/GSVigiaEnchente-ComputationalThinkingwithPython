#Alexandre Freitas Silva RM:566278
#Artur Distrutti Santos RM:561319
#Felipe Rodrigues Gomes Ribeiro RM:562482


#função para calcular os mantimentos necessários.
def calcular_necessidades(pessoas, dias=1):
    agua_total = 2 * pessoas * dias   # calcular o tanto de água necessário para os dias.
    comida_total = 3 * pessoas * dias   # calcular o tanto de refeições necessário para os dias.
    return agua_total, comida_total #retorna as quantidades necessárias respectivamente.

#função para exibir a lista
def mostrar_lista(pessoas, dias, lista_extra):
    if pessoas == 0 or dias == 0:  #checando pra ver se já foi colocado o número de pessoas e dias
        print("Por favor, defina o número de pessoas e dias primeiro.\n")
        return
    #prints para aparecer na tela
    print(f"\n--- Informações do Kit de Emergência ---")
    print(f"Número de pessoas: {pessoas}")
    print(f"Dias planejados: {dias}")
    agua, comida = calcular_necessidades(pessoas, dias) #puxando a função que calcula necessidades
    print(f"Água necessária: {agua} litros")
    print(f"Refeições necessárias: {comida} refeições")

    #exibir  a lista extra de equipamentos
    if lista_extra:
        print("Itens extras adicionados:")
        for i, item in enumerate(lista_extra, 1): #exibir os itens adicionados e quantidades
            print(f"{i}. {item['item']} - Quantidade: {item['quantidade']}")
    else:
        print("Nenhum item extra adicionado.")#caso não tenha itens adiconados
    print("----------------------------------------\n")

def main():
    print("=== Planejador de Kit de Emergência ===\n") 

    lista_extra = [] #lista dos itens extras

    while True:
        try:
            pessoas = int(input("Digite o número de pessoas: "))
            dias = int(input("Digite o número de dias: "))
            if pessoas > 0 and dias > 0:
                break #quebra se inseridos numeros de dias e pessoas
            else:
                print("Por favor, insira números positivos.\n") #caso insira numeros negativos
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.\n") #caso insira numeros quebrados

    while True:
        print("\nEscolha uma opção:") #exibição das opções no terminal
        print("1. Mostrar lista atual")
        print("2. Adicionar item extra")
        print("3. Sair")

        opcao = input("Opção: ") #escolha da opção

        if opcao == "1":
            mostrar_lista(pessoas, dias, lista_extra)

        elif opcao == "2":
            nome_item = input("Nome do equipamento extra: ").strip() #nome do equipamento
            if not nome_item:
                print("Nome inválido. Tente novamente.") #caso não tenha inserido nome algum
                continue
            try:
                qtd = int(input("Quantidade: ")) #quantidade do equipamento selecionado
                if qtd <= 0:
                    print("Quantidade precisa ser maior que 0.") #caso insera o nome do equipamento mas uma quantidade invalida
                    continue
                lista_extra.append({"item": nome_item, "quantidade": qtd}) #adiciona o equipamento a lista
                print(f"Item '{nome_item}' adicionado com sucesso.")
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro.")

        elif opcao == "3":
            print("Saindo do planejador. Fique seguro!") #saindo do planejador
            break

        else:
            print("Opção inválida. Tente novamente.") #caso escolha nenhuma das 3 opções.

if __name__ == "__main__":
    main()
##esse código no projeto principal foi feito com streamlit para rodar na web(se quiser ver rodando web é só ir pro site principal, aqui só vai rodar no console❤), esse aqui é a versão sem a biblioteca streamlit, porém os dois são iguais.