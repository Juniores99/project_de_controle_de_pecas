listPecas = [] # cria uma lista de "pecas"

def cadastroPeca(codigo): #funcao para cadastro de pecas com argumento "codigo"
    print('Cadastrar peça')
    print('O codigo da peça é {:.2f}'.format(codigo))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    preco = float(input('Digite o preço da peça (em R$): '))

    pecaInfo = {'codigo':codigo, # em pecaInfo o objetivo é dar atributos para cada opção da peça
                'nome': nome,
                'fabricante':fabricante,
                'preco':preco
                } # seus atributos serão usados psteriormente
    listPecas.append(pecaInfo.copy()) #metodo append com argumento para adiconar um determinado valor

def consultarPeca(): #função para consulta das peças
    while True: # laço que será executado conforme a condição booleana for verdadeira
        try: # implementando Try e except para o bom funcinamento do código em caso de erro
            print('Consultar peça')
            consulta = int(input('Escolha a opção desejada:\n'
                                 '1 - Consultar todas as peças\n'
                                 '2 - Consultar peça por código\n'
                                 '3 - Consultar peça por fabricante\n'
                                 '4 - Retornar\n'
                                 '---> ')) # após apresentar as opçoes irá capturar a opção do usuario
            if consulta == 1:
                print('-' * 20)
                for pecas in listPecas:
                    for key, value in pecas.itens():
                        print('{} : {}'.format(key, value))# metodo format que usa key e value respectivamente para atribuição
                    print('-'* 20)# apenas uma maneira de imprimir --- vinte vezes

            elif consulta == 2:
                print('Voce escolheu consultar por código')
                entrada = int(input('Digite o código do produto: '))
                print('-' * 20)
                for pecas in listPecas:
                    if (pecas['codigo'] == entrada): #aqui chama o primeiro atributo mencionado em pecaInfo
                        for key, value in pecas.itens():
                            print('{} : {}'.format(key, value))
                        print('-' * 20)

            elif consulta == 3:
                print('Voce escolheu consultar por fabricante')
                entrada = input('Digite o nome do fabricante: ')
                print('-' * 20)
                for pecas in listPecas:
                    if (pecas['fabricante'] == entrada):
                        for key, value in pecas.itens():
                            print('{} : {}'.format(key, value))
                        print('-' * 20)

            elif consulta == 4:
                break
            else:
                print('Digite apenas o que é pedido')
                continue

        except ValueError:
            print('Não digite numeros que não existem')
            continue

def removerPeca(): # funão de remover peça qie funciona com metodo .remove
    print('Voce selecionou remover peças')
    entrada = int(input('Digite o código da peça que deseja remover: '))
    for pecas in listPecas:
        if (pecas['codigo'] == entrada):
            listPecas.remove(pecas)
        else:
            print('Você removeu a peça')
print('Bem vindo ao controle de estoque de peças')
registroPecas = 0

while True: #laço que será executado para dar as opções iniciais do usuaário
    try:
        opcao = int(input('Digite uma opcao desejada:\n'
                          '1 - Cadastrar peça \n'
                          '2 - Consultar peça \n'
                          '3 - Remover peça \n'
                          '4 - Sair \n'
                          '---> '))# as opções primárias são baseadas nas operações básicas feitas no começo do código
        if opcao == 1: # cada condição chama uma determindada funcção
            registroPecas +=1
            cadastroPeca((registroPecas))
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Fim')
            break
        else:
            print('Digite somente uma das opções do Menu')
            continue
    except ValueError:
        print('Não digite numeros inexistentes')
