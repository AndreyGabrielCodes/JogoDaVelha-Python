def valida_per(text_per, tipo, min=0, max=0):
    """
    Função para validar a entrada do usuário com tipo e intervalo definidos.

    - tipo: define se a entrada é texto (str) ou número (int ou float).
    - minimo e maximo: definem o intervalo para valores numéricos (opcional).
    """
    while True:
        try:
            if tipo in (int, float):
                resposta = float(input(text_per))
                if min <= resposta <= max:
                    return int(resposta)
                else:
                    system('cls')
                    menu()
                    print(f'*Linha ou coluna fora do intervalo existente!\n')
            elif tipo == str:
                resposta = input(text_per)
                if len(resposta) >= 1:
                    return resposta
                else:
                    system('cls')
                    print('*Tipo de valor inválido')
            elif tipo == 'menu':
                resposta = float(input(text_per))
                if min <= resposta <= max:
                    return int(resposta)
                else:
                    print(f'*Valor fora do intervalo: {min} a {max}')
            else:
                system('cls')
                menu()
                raise TypeError('*Tipo de valor inválido')
        except ValueError:
            print('*Tipo de valor inválido')


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
    numero_combinacao = 1
    while(True):
        combinacao_feita = ''
        posicoes_ocupadas = 0
        match numero_combinacao:
            #verifica linhas
            case 1:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (1,2,3)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 2:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (4,5,6)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 3:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (7,8,9)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            #verifica colunas
            case 4:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (1,4,7)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 5:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (2,5,8)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 6:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (3,6,9)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            #verifica diagonais
            case 7:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (1,5,9)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 8:
                for posicao in lista_todas_posicoes:
                    if ((posicao['id'] in (3,5,7)) and posicao['simbolo'] in ('X','O')):
                        combinacao_feita += posicao['simbolo']
            case 9:
                 #todas posicoes ocupadas
                for posicao in lista_todas_posicoes:
                    if (posicao['ocupada'] == 1):
                        posicoes_ocupadas += 1
            case 10:
                break

        if (combinacao_feita in ('XXX','OOO')):
            if(combinacao_feita == 'XXX'):
                jogador_x[3] = 1
                status = 2
                break
            else:
                jogador_o[3] = 1
                status = 2
                break
        elif (posicoes_ocupadas == 9):
            status = 1
            break
        else:
            numero_combinacao += 1
    return status

def atribui_posicao(linha, coluna, simbolo):
    valido = False
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
        coluna_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma coluna: ',int,1,3)
        linha_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma linha: ',int,1,3)
        repete_escolha = atribui_posicao(linha_escolhida, coluna_escolhida, simbolo_ult_jog) 

def menu():
    menu = ''
    id_posicao = 1
    lista_exibe_pos = []
    while(id_posicao < 10):
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id_posicao):
                lista_exibe_pos.append(posicao['simbolo'])
        id_posicao += 1
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
modo_jogo = valida_per('Escolha um modo de jogo: ','menu',1,2)
if(modo_jogo == 1):
    jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
    jogador_o[1] = valida_per('| Nome do Jogador que será o O: ',str)
else:
    system('cls')
    print('| DIFICULDADE |')
    print('| 1 - Fácil   |')
    print('| 2 - Médio   |')
    print('| 3 - Dificil |\n')
    dificuldade_computador = valida_per('Escolha um modo de jogo: ','menu',1,3)
    jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
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
    reseta_partida = valida_per('\nDeseja iniciar uma nova partida ? (1/0): ','menu',0,1)
    if(reseta_partida == 1):
        reseta_posicoes()
        primeira_jogada = True
        continue
    else:
        break
system('cls')
print('Jogo finalizado, obrigado por jogar !')