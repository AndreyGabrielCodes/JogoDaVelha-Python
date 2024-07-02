def turno_computador():
    print

def pontos_partida():
    print

def status_partida():
    print

def atribui_posicao():
    print

def verifica_pos_val(jog_ult_jogada):
    print

def jogador_turno_atual():
    global jogador01
    global jogador02
    global jog_ult_jogada
    vez_jogada = ''
    
    if (jog_ult_jogada == 'jog1'):
        vez_jogada = jogador02[1]
        jog_ult_jogada = 'jog2'
    else:
        vez_jogada = jogador01[1]
        jog_ult_jogada = 'jog1'
    input(f'Escolha uma posição {vez_jogada}: ')
    verifica_pos_val(jog_ult_jogada)
    
#controles globais de jogada
jog_ult_jogada = 'jog2' #jogador 01 como inicial


#controle de posição
    #indice 0 é para ocupação da posição quando igual a 1
    #indice 1 é para preenchimento do simbolo inserido
    #variavel_x_y - X é linha e Y é coluna - valido para os controles de combinação
posicao_1_1 = [0,'']
posicao_1_2 = [0,'']
posicao_1_3 = [0,'']

posicao_2_1 = [0,'']
posicao_2_2 = [0,'']
posicao_2_3 = [0,'']

posicao_3_1 = [0,'']
posicao_3_2 = [0,'']
posicao_3_3 = [0,'']

#controle de combinação
vertical_1_1 = posicao_1_1[0] + posicao_2_1[0] + posicao_3_1[0]
vertical_1_2 = posicao_1_2[0] + posicao_2_2[0] + posicao_3_2[0]
vertical_1_3 = posicao_1_3[0] + posicao_2_3[0] + posicao_3_3[0]

horizontal_1_1 = posicao_1_1[0] + posicao_1_2[0] + posicao_1_3[0]
horizontal_1_2 = posicao_2_1[0] + posicao_2_2[0] + posicao_2_3[0]
horizontal_1_3 = posicao_3_1[0] + posicao_3_2[0] + posicao_3_3[0]

diagonal_1 = posicao_1_1[0] + posicao_2_2[0] + posicao_3_3[0]
diagonal_2 = posicao_1_3[0] + posicao_2_2[0] + posicao_3_1[0]


#variáveis de jogadores
jogador01 = [0,''] #pontuação e nome
jogador02 = [0,'']

#programa principal
jogador01[1] = input('Digite o nome do primeiro jogador: ')
jogador02[1] = input('Digite o nome do segundo jogador: ')
input('Enter para iniciar')

while(True):
    jogador_turno_atual()