def turno_computador():
    print

def pontos_partida():
    print

def status_partida():
    print

def atribui_posicao(linha,coluna):
    print

def verifica_pos_val(linha, coluna):
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
            print('Posição escolhida com sucesso!')
            valido = True
    return valido

def jogador_turno_atual():
    global jogador_x
    global jogador_o
    global jog_ult_jogada
    
    if (jog_ult_jogada == jogador_x[1]):
        jog_ult_jogada = jogador_o[1]
    else:
        jog_ult_jogada = jogador_x[1]

    repete_escolha = False
    while(repete_escolha == False):
        linha = 0
        coluna = 0
        linha = int(input(f'{jog_ult_jogada}, escolha uma linha: '))
        coluna = int(input(f'{jog_ult_jogada}, escolha uma coluna: '))
        repete_escolha = verifica_pos_val(linha, coluna)
    atribui_posicao(linha, coluna)
    
#controle de posição
posicao_1_1 = {'ocupada':0,'simbolo':'','linha':1,'coluna':1}
posicao_1_2 = {'ocupada':0,'simbolo':'','linha':1,'coluna':2}
posicao_1_3 = {'ocupada':0,'simbolo':'','linha':1,'coluna':3}

posicao_2_1 = {'ocupada':0,'simbolo':'','linha':2,'coluna':1}
posicao_2_2 = {'ocupada':0,'simbolo':'','linha':2,'coluna':2}
posicao_2_3 = {'ocupada':0,'simbolo':'','linha':2,'coluna':3}

posicao_3_1 = {'ocupada':0,'simbolo':'','linha':3,'coluna':1}
posicao_3_2 = {'ocupada':0,'simbolo':'','linha':3,'coluna':2}
posicao_3_3 = {'ocupada':0,'simbolo':'','linha':3,'coluna':3}

lista_todas_posicoes = [posicao_1_1, posicao_1_2, posicao_1_3, posicao_2_1, posicao_2_2, posicao_2_3, posicao_3_1, posicao_3_2, posicao_3_3]

#controle de combinação
vertical_1_1 = posicao_1_1['ocupada'] + posicao_2_1['ocupada'] + posicao_3_1['ocupada']
vertical_1_2 = posicao_1_2['ocupada'] + posicao_2_2['ocupada'] + posicao_3_2['ocupada']
vertical_1_3 = posicao_1_3['ocupada'] + posicao_2_3['ocupada'] + posicao_3_3['ocupada']

horizontal_1_1 = posicao_1_1['ocupada'] + posicao_1_2['ocupada'] + posicao_1_3['ocupada']
horizontal_1_2 = posicao_2_1['ocupada'] + posicao_2_2['ocupada'] + posicao_2_3['ocupada']
horizontal_1_3 = posicao_3_1['ocupada'] + posicao_3_2['ocupada'] + posicao_3_3['ocupada']

diagonal_1 = posicao_1_1['ocupada'] + posicao_2_2['ocupada'] + posicao_3_3['ocupada']
diagonal_2 = posicao_1_3['ocupada'] + posicao_2_2['ocupada'] + posicao_3_1['ocupada']


#variáveis de jogadores
jogador_x = [0,''] #pontuação e nome
jogador_o = [0,'']

#controles globais de jogada
jog_ult_jogada = jogador_o[1] #jogador 01 como inicial


#programa principal
jogador_x[1] = input('Nome do Jogador que será o X: ')
jogador_o[1] = input('Nome do Jogador que será o O: ')
print(f'{jogador_x[1]} inicia a partida!')
input('Enter para iniciar')

while(True):
    jogador_turno_atual()