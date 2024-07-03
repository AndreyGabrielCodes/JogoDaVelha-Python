def turno_computador():
    print

def pontos_partida():
    print

def status_partida():
    horizontal_1 = 0
    horizontal_2 = 0
    horizontal_3 = 0
    vertical_1 = 0
    vertical_2 = 0
    vertical_3 = 0
    diagonal_1 = 0
    diagonal_2 = 0
    todas_posicoes_ocupadas = 0

def atribui_posicao(linha, coluna, simbolo):
    valido = False
    if ((linha > 3 or linha < 1) and (coluna > 3 or coluna < 1)):
        valido = False
        print('Linha ou coluna fora do intervalo existente!')
    else:
        posicao_ocupada = 0
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                posicao_ocupada = posicao['ocupada']
        if (posicao_ocupada == 1):
            print('Posição escolhida está ocupada pelo outro jogador!')
            valido = False
        else:
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = simbolo
            print('Posição escolhida com sucesso!')
            valido = True
    return valido

def jogador_turno_atual():
    global jogador_x
    global jogador_o
    global jog_ult_jogada
    global simbolo_ult_jog
    if (jog_ult_jogada == jogador_x[1]):
        jog_ult_jogada = jogador_o[1]
        simbolo_ult_jog = jogador_o[2]
    else:
        jog_ult_jogada = jogador_x[1]
        simbolo_ult_jog = jogador_x[2]
    repete_escolha = False
    while(repete_escolha == False):
        linha = 0
        coluna = 0
        linha = int(input(f'{jog_ult_jogada}, escolha uma linha: '))
        coluna = int(input(f'{jog_ult_jogada}, escolha uma coluna: '))
        repete_escolha = atribui_posicao(linha, coluna, simbolo_ult_jog)

def menu():
    menu = ''
    posicao1_1 = ' '
    posicao1_2 = ' '
    posicao1_3 = ' '
    posicao2_1 = ' '
    posicao2_2 = ' '
    posicao2_3 = ' '
    posicao3_1 = ' '
    posicao3_2 = ' '
    posicao3_3 = ' '
    for posicao in lista_todas_posicoes:
        #verificar depois se é possível encurtar esta função fazendo a comparação de linha e coluna 
        # virarem variaveis que vão alterando os valores compreendendo cada posicao
        #linha 1
        if ((posicao['linha'] == 1) and (posicao['coluna'] == 1)):
            posicao1_1 = posicao['simbolo']
        elif ((posicao['linha'] == 1) and (posicao['coluna'] == 2)):
            posicao1_2 = posicao['simbolo']
        elif ((posicao['linha'] == 1) and (posicao['coluna'] == 3)):
            posicao1_3 = posicao['simbolo']
        #linha 2
        elif ((posicao['linha'] == 2) and (posicao['coluna'] == 1)):
            posicao2_1 = posicao['simbolo']
        elif ((posicao['linha'] == 2) and (posicao['coluna'] == 2)):
            posicao2_2 = posicao['simbolo']
        elif ((posicao['linha'] == 2) and (posicao['coluna'] == 3)):
            posicao2_3 = posicao['simbolo']
        #linha 3
        elif ((posicao['linha'] == 3) and (posicao['coluna'] == 1)):
            posicao3_1 = posicao['simbolo']
        elif ((posicao['linha'] == 3) and (posicao['coluna'] == 2)):
            posicao3_2 = posicao['simbolo']
        elif ((posicao['linha'] == 3) and (posicao['coluna'] == 3)):
            posicao3_3 = posicao['simbolo']
    menu = f"""|{posicao1_1}|{posicao1_2}|{posicao1_3}|\n|{posicao2_1}|{posicao2_2}|{posicao2_3}|\n|{posicao3_1}|{posicao3_2}|{posicao3_3}|\n"""
    print(menu)


#cadastro de posicoes
lista_todas_posicoes = [{'ocupada':0,'simbolo':' ','linha':1,'coluna':1}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':2}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':3}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':1}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':2}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':3}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':1}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':2}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':3}]

#variáveis de jogadores
jogador_x = [0,'','X'] #pontuação, nome, simbolo
jogador_o = [0,'','O']

#controles globais de jogada
jog_ult_jogada = jogador_o[1] #jogador 01 como inicial
simbolo_ult_jog = jogador_o[2]

from os import system

#programa principal
jogador_x[1] = input('Nome do Jogador que será o X: ')
jogador_o[1] = input('Nome do Jogador que será o O: ')
print(f'{jogador_x[1]} inicia a partida!')
input('Enter para iniciar')

while(True):
    system('cls')
    status_partida()
    menu()
    jogador_turno_atual()
