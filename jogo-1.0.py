def turno_computador():
    print

def pontos_partida():
    print

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
        print('Linha ou coluna fora do intervalo existente!')
    else:
        posicao_ocupada = 0
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                posicao_ocupada = posicao['ocupada']
        if (posicao_ocupada == 1):
            print('Posição escolhida está ocupada! Tente novamente')
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
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]

#controles globais de jogada
jog_ult_jogada = jogador_o[1] #jogador 01 como inicial
simbolo_ult_jog = jogador_o[2]

from os import system

#programa principal
system('cls')
jogador_x[1] = input('Nome do Jogador que será o X: ')
jogador_o[1] = input('Nome do Jogador que será o O: ')
print('')
print(f'{jogador_x[1]} inicia a partida!')
print('')
input('Enter para iniciar')

while(status_partida() == 0): #repetirá enquanto a partida estiver com status de jogo acontecendo
    system('cls')
    menu()
    jogador_turno_atual()

resultado = ''
system('cls')
if((jogador_x[3] == 0) and (jogador_o[3] == 0)):
     resultado = ('Empate! Nenhum jogador ganhou')
else:
    if (jogador_x[3] == 1):
        resultado = (f'Vitoria de {jogador_x[1]} que escolheu {jogador_x[2]}!')
    elif (jogador_o[3] == 1):
        resultado = (f'Vitoria de {jogador_o[1]} que escolheu {jogador_o[2]}!')

print(f'Resultado da partida: {resultado}')