def turno_computador():
    """
    Primeiro o computador verifica se o jogador oponente falta uma posicao para fechar uma combinação de vitória
     e o tenta barrar
    Caso não, verifica combinações possíveis, escolhe uma, e começa a completá-la
    """
    #checa posicao escolhida pelo oponente

        #jogador iniciou em um dos cantos

    #checa combinações possíveis de fazer





    combinacao_escolhida = 0

def reseta_posicoes():
    for posicao in lista_todas_posicoes:
        if (posicao['ocupada'] == 1):
            posicao['ocupada'] = 0
            posicao['simbolo'] = ' '

def status_partida():
    todas_posicoes_ocupadas = 0
    status = 0 #status da partida
        #status = 0 = jogo acontecendo
        #status = 1 = empate
        #status = 2 = vitoria
    combinacao_feita = ''
    posicoes_ocupadas = 0
    #verifica combinações de vitória possível e retorna status
        #soma a combinacao_feita a combinação e caso não seja vitória
        # limpa a variavel e passa para a próxima combinação
    #linha 1
    for posicao in lista_todas_posicoes:
        if (((posicao['linha'] == 1) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #linha 2
    for posicao in lista_todas_posicoes:
        if (((posicao['linha'] == 2) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #linha 3
    for posicao in lista_todas_posicoes:
        if (((posicao['linha'] == 3) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #vertical 1
    for posicao in lista_todas_posicoes:
        if (((posicao['coluna'] == 1) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #vertical 2
    for posicao in lista_todas_posicoes:
        if (((posicao['coluna'] == 2) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #vertical 3
    for posicao in lista_todas_posicoes:
        if (((posicao['coluna'] == 3) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #diagonal 1
    for posicao in lista_todas_posicoes:
        if (((posicao['linha'] == 1) and (posicao['coluna'] == 1) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
        elif (((posicao['linha'] == 2) and (posicao['coluna'] == 2) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
        elif (((posicao['linha'] == 3) and (posicao['coluna'] == 3) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #diagonal 2
    for posicao in lista_todas_posicoes:
        if (((posicao['linha'] == 1) and (posicao['coluna'] == 3) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
        elif (((posicao['linha'] == 2) and (posicao['coluna'] == 2) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
        elif (((posicao['linha'] == 3) and (posicao['coluna'] == 1) and (posicao['ocupada'] == 1) and 
             ((posicao['simbolo'] == 'X') or (posicao['simbolo'] == 'O')))):
            combinacao_feita += posicao['simbolo']
    if (combinacao_feita == 'XXX'):
        status = 2
        jogador_x[3] = 1
    elif (combinacao_feita == 'OOO'):
        status = 2
        jogador_o[3] = 1
    else:
        combinacao_feita = ''
    #todas posicoes ocupadas
    for posicao in lista_todas_posicoes:
        if (posicao['ocupada'] == 1):
            posicoes_ocupadas += 1
    if (posicoes_ocupadas == 9):
        status = 1
    else:
        posicoes_ocupadas = 0
    return status


def atribui_posicao(linha, coluna, simbolo):
    valido = False
    if ((linha > 3 or linha < 1) and (coluna > 3 or coluna < 1)):
        valido = False
        print('\nLinha ou coluna fora do intervalo existente!\n')
    else:
        posicao_ocupada = 0
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                posicao_ocupada = posicao['ocupada']
        if (posicao_ocupada == 1):
            print('\nPosição escolhida está ocupada! Tente novamente\n')
            valido = False
        else:
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = simbolo
            print('Posição escolhida com sucesso!')
            valido = True
    return valido

def jogador_turno_atual(modo_jogo):
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
    #modo jogador x computador
    if((modo_jogo == 2) and jog_ult_jogada == jogador_o[1]):
        turno_computador()
    else:
        #modo jogador x jogador
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

def jogador_inicio_partida(modo_jogo):
    #aleatoriza o jogador que inicia a partida
    global jog_ult_jogada
    global simbolo_ult_jog
    jogadores = []
    simbolos_jogadores = []
    if (modo_jogo == 1):
        jogadores = [jogador_x[1],jogador_o[1]]
        simbolos_jogadores = [jogador_x[2],jogador_o[2]]
        aleatorio = random.randint(0,1)
        jog_ult_jogada = jogadores[aleatorio]
        simbolo_ult_jog = simbolos_jogadores[aleatorio]
    else:
        jog_ult_jogada = jogador_o[1]
        simbolo_ult_jog = 'O'

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
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]

#controles globais de jogada
jog_ult_jogada = ''
simbolo_ult_jog = ''

from os import system
import random

#programa principal
system('cls')
print('|      JOGO DA VELHA       |')
print('|                          |')
print('|       MODO DE JOGO       |')
print('| 1 - Jogador x Jogador    |')
print('| 2 - Jogador x Computador |\n')
modo_jogo = int(input('Escolha um modo de jogo: '))
if(modo_jogo == 1):
    jogador_x[1] = input('\n| Nome do Jogador que será o X: ')
    jogador_o[1] = input('| Nome do Jogador que será o O: ')
else:
    print('Ainda não configurado!')
while(True):
    system('cls')
    print(f'{jog_ult_jogada} inicia a partida!\n')
    jogador_inicio_partida(modo_jogo)
    input('Enter para iniciar partida')
    while(status_partida() == 0): #repetirá enquanto a partida estiver com status de jogo acontecendo
        system('cls')
        menu()
        jogador_turno_atual(modo_jogo)
    resultado = ''
    system('cls')
    if((jogador_x[3] == 0) and (jogador_o[3] == 0)):
        resultado = ('Empate! Nenhum jogador ganhou')
    else:
        if (jogador_x[3] == 1):
            resultado = (f'Vitoria de {jogador_x[1]} que escolheu {jogador_x[2]}!')
            jogador_x[0] += 1
        elif (jogador_o[3] == 1):
            resultado = (f'Vitoria de {jogador_o[1]} que escolheu {jogador_o[2]}!')
            jogador_o[0] += 1
    print(f'| Resultado da partida: {resultado}\n')
    print(f'| Pontuações:\n- {jogador_x[1]}: {jogador_x[0]}\n-{jogador_o[1]}: {jogador_o[0]}')
    reseta_partida = int(input('\nDeseja iniciar uma nova partida ? (1/0): '))
    if(reseta_partida == 1):
        reseta_posicoes()
        continue
    else:
        break
system('cls')
print('Jogo finalizado, obrigado por jogar !')