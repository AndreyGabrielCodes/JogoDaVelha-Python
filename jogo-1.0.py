def turno_computador(dificuldade):
    """
    Primeiro o computador verifica se o jogador oponente falta uma posicao para fechar uma combinação de vitória
     e o tenta barrar
    Caso não, verifica combinações possíveis, escolhe uma, e começa a completá-la
    Dificuldades:
    1 - Facil - Joga em posicoes aleatórias
    2 - Medio - Joga para formar combinações
    3 - Dificil - Joga tentando bloquear o jogador
    """
    #verifica posicoes validas para o computador trabalhar em cima
    lista_posicoes_validas = []
    lista_posicoes_validas.clear()
    for posicao in lista_todas_posicoes:
        if(posicao['ocupada'] == 0):
                lista_posicoes_validas.append(posicao['id'])

    match dificuldade:
        case 1: #facil
            posicao_escolhida = 0
            posicao_escolhida = random.choice(lista_posicoes_validas)
            for posicao in lista_todas_posicoes:
                if (posicao['id'] == posicao_escolhida):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = 'O'
        case 2: #medio
            print
        case 3: # dificil 
            print

def reseta_posicoes():
    for posicao in lista_todas_posicoes:
        if (posicao['ocupada'] == 1):
            posicao['ocupada'] = 0
            posicao['simbolo'] = ' '

def status_partida():
    status = 0 #status da partida
        #status = 0 = jogo acontecendo
        #status = 1 = empate
        #status = 2 = vitoria
    posicoes_ocupadas = 0
    sentido_posicao = 'linha'
    numero_posicao = 1

    #verifica combinações de vitória possível e retorna status
    while(True):
        combinacao_feita = ''
        #verifica posicoes ocupadas pelos simbolos no sentido "linha" e "coluna"
        if (sentido_posicao in ('linha','coluna')):
            for posicao in lista_todas_posicoes:
                if ((posicao[sentido_posicao] == numero_posicao) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
        #verifica posicoes ocupadas pelos simbolos no sentido "diagonal"
        elif(sentido_posicao == 'diagonal1'):
            #diagonal esquerda para direita
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == 1) and (posicao['coluna'] == 1) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
                elif ((posicao['linha'] == 2) and (posicao['coluna'] == 2) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
                elif ((posicao['linha'] == 3) and (posicao['coluna'] == 3) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
        elif(sentido_posicao == 'diagonal2'):
            #diagonal direita para esquerda
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == 1) and (posicao['coluna'] == 3) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
                elif ((posicao['linha'] == 2) and (posicao['coluna'] == 2) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
                elif ((posicao['linha'] == 3) and (posicao['coluna'] == 1) and (posicao['simbolo'] in ('X','O'))):
                    combinacao_feita += posicao['simbolo']
        #altera os sentidos e posicoes conforme as posicoes forem verificadas
        if((sentido_posicao == 'linha') and(numero_posicao < 3)):
            numero_posicao += 1
        #quando as 3 posicoes no sentido "linha" foram feitas, 
        # é alterado o sentido para "coluna" e resetado o valor do numero_posicao
        elif((sentido_posicao == 'linha') and(numero_posicao == 3)):
            numero_posicao = 1
            sentido_posicao = 'coluna'
        elif((sentido_posicao == 'coluna') and(numero_posicao < 3)):
            numero_posicao += 1
        #quando as 3 posicoes no sentido "coluna" foram feitas, 
        # é alterado o sentido para "diagonal" e resetado o valor do numero_posicao
        elif((sentido_posicao == 'coluna') and(numero_posicao == 3)):
            numero_posicao = 1
            sentido_posicao = 'diagonal1'
        elif((sentido_posicao == 'diagonal1') and(numero_posicao < 2)):
            numero_posicao += 1
        #quando a primeira diagonal foi feita, parte para a segunda
        elif((sentido_posicao == 'diagonal1') and(numero_posicao == 2)):
            numero_posicao = 1
            sentido_posicao = 'diagonal2'
        elif((sentido_posicao == 'diagonal2') and(numero_posicao < 2)):
            numero_posicao += 1
        #quando as diagonais foram vistas mas não retornaram vitoria, interrompe o laço
        elif((sentido_posicao == 'diagonal2') and(numero_posicao == 2)):
            break

        #verifica a combinacao feita
        if (combinacao_feita == 'XXX'):
            status = 2
            jogador_x[3] = 1
            break
        elif (combinacao_feita == 'OOO'):
            status = 2
            jogador_o[3] = 1
            break

    #todas posicoes ocupadas
    if(combinacao_feita not in ('XXX','OOO')):
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
    if ((linha > 3 or linha < 1) or (coluna > 3 or coluna < 1)):
        valido = False
        system('cls')
        menu()
        print('*Linha ou coluna fora do intervalo existente!\n')
    else:
        posicao_ocupada = 0
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha) and (posicao['coluna'] == coluna)):
                posicao_ocupada = posicao['ocupada']
        if (posicao_ocupada == 1):
            system('cls')
            menu()
            print('*Posição escolhida está ocupada! Tente novamente\n')
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
    global primeira_jogada
    global dificuldade_computador
    #verifica se é a primeira jogada para manter o jogador que foi selecionado pela função "jogador_inicio_partida" 
    # ou se o modo é "jogador x computador" para sempre começar com o jogador
    if (((modo_jogo in (1,2)) and (primeira_jogada == True)) or ((modo_jogo == 1) and (primeira_jogada == True))):
        escolhe_posicao()
        primeira_jogada = False
    #modo jogador x jogador - altera o jogador conforme o ultimo que jogou
    elif ((modo_jogo == 1)):
        if ((jog_ult_jogada == jogador_x[1])):
            jog_ult_jogada = jogador_o[1]
            simbolo_ult_jog = jogador_o[2]
            escolhe_posicao()
        else:
            jog_ult_jogada = jogador_x[1]
            simbolo_ult_jog = jogador_x[2]
            escolhe_posicao()
    #modo jogador x computador - altera o jogador conforme o ultimo que jogou
    elif ((modo_jogo == 2)):
        if(jog_ult_jogada == jogador_x[1]):
            turno_computador(dificuldade_computador)
            jog_ult_jogada = jogador_o[1]
            simbolo_ult_jog = 'O'
        else:
            jog_ult_jogada = jogador_x[1]
            simbolo_ult_jog = 'X'
            escolhe_posicao()

def escolhe_posicao():
   repete_escolha = False
   #repete a escolha das posicoes conforme retorno true ou false da função "atribui_posicao"
   while(repete_escolha == False):
        coluna_escolhida = int(input(f'{jog_ult_jogada}, escolha uma coluna: '))
        linha_escolhida = int(input(f'{jog_ult_jogada}, escolha uma linha: '))
        repete_escolha = atribui_posicao(linha_escolhida, coluna_escolhida, simbolo_ult_jog) 

def menu():
    menu = ''
    id_posicao = 1
    lista_exibe_pos = []
    while(True):
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id_posicao):
                lista_exibe_pos.append(posicao['simbolo'])
        id_posicao += 1
        if(id_posicao > 9):
            break
    menu = f'JOGO DA VELHA 1.0\n\n Coluna x Linha\n      1 2 3  \n    1|{lista_exibe_pos[0]}|{lista_exibe_pos[1]}|{lista_exibe_pos[2]}|\n    2|{lista_exibe_pos[3]}|{lista_exibe_pos[4]}|{lista_exibe_pos[5]}|\n    3|{lista_exibe_pos[6]}|{lista_exibe_pos[7]}|{lista_exibe_pos[8]}|\n'
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
        jog_ult_jogada = jogador_x[1]
        simbolo_ult_jog = 'X'
    print(f'{jog_ult_jogada} inicia a partida!\n')

#cadastro de posicoes
lista_todas_posicoes = [{'ocupada':0,'simbolo':' ','linha':1,'coluna':1,'id':1}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':2,'id':2}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':3,'id':3}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':1,'id':4}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':2,'id':5}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':3,'id':6}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':1,'id':7}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':2,'id':8}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':3,'id':9}]

#variáveis de jogadores
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]

#controles globais de jogada
jog_ult_jogada = ''
simbolo_ult_jog = ''

primeira_jogada = True
dificuldade_computador = 0

resultado = ''

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
    system('cls')
    print('| DIFICULDADE |')
    print('| 1 - Fácil   |')
    print('| 2 - Médio   |')
    print('| 3 - Dificil |\n')
    dificuldade_computador = int(input('Escolha um modo de jogo: '))
    jogador_x[1] = input('\n| Nome do Jogador que será o X: ')
    jogador_o[1] = 'Computador'
while(True):
    system('cls')
    jogador_inicio_partida(modo_jogo)
    input('Enter para iniciar partida')
    while(status_partida() == 0): #repetirá enquanto a partida estiver com status de jogo acontecendo
        system('cls')
        menu()
        jogador_turno_atual(modo_jogo)
    system('cls')
    menu()
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
    print(f'| Pontuações:\n| - {jogador_x[1]}: {jogador_x[0]}\n| - {jogador_o[1]}: {jogador_o[0]}')
    reseta_partida = int(input('\nDeseja iniciar uma nova partida ? (1/0): '))
    if(reseta_partida == 1):
        reseta_posicoes()
        primeira_jogada = True
        continue
    else:
        break
system('cls')
print('Jogo finalizado, obrigado por jogar !')