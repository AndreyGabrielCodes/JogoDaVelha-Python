def pc_turno():

    """#criar verificação dupla que verifica se o jogador pode ganhar em casos onde 
    # ao tentar bloquear uma combinação a outra vence
    # fazer com que o computador responda forçando o jogador a bloqueá-lo

    id_jog_usu = [] #recebe até 3 jogadas
    num_jog_usu = 0

    #insere o id das posicoes das 3 primeiras jogadas do jogador
    for posicao in lista_todas_posicoes:
        if((posicao['ocupada'] == 1) and (posicao['simbolo'] == 'X')):
            num_jog_usu += 1
            if(num_jog_usu < 3):
                id_jog_usu.append(posicao['id'])"""

    while(True):
        global pc_id_alea_comb_jog
        global pc_comb_atual
        #cadastro de preenchimento das posições da combinação escolhida pelo computador
        lista_ocupa_pos_comb_atual = [
            {'id':1,'id_pos':0,'ocupada':0},
            {'id':2,'id_pos':0,'ocupada':0},
            {'id':3,'id_pos':0,'ocupada':0}]
        
        
        #gera combinações possíveis
        pc_comb()
        lista_comb_possiveis.clear()
        for comb in lista_pc_comb:
            if (comb['valido'] == 1):
                lista_comb_possiveis.append(comb['id'])
        #caso todas as combinações estejam indisponíveis
        # altera para o computador jogador aleatoriamente
        if (lista_comb_possiveis == []):
            pc_comb_atual = 0
            #lista todas as posições disponíveis para o modo aleatório
            lista_pos_val_modo_alea.clear()
            for posicao in lista_todas_posicoes:
                if(posicao['ocupada'] == 0):
                    lista_pos_val_modo_alea.append(posicao['id'])
            #escolhe aleatoriamente uma das posições e joga
            posicao_escolhida = 0
            posicao_escolhida = random.choice(lista_pos_val_modo_alea)
            for posicao in lista_todas_posicoes:
                if (posicao['id'] == posicao_escolhida):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = 'O'
            break
        else:
            #caso o computador já tenha escolhido uma combinação
            # não é aleatorizado uma nova
            if (pc_comb_atual == 0):
                pc_comb_atual = random.choice(lista_comb_possiveis)
        #estrutura de escolha da posição de jogada do computador
        if ((pc_comb_atual != 0)):
            #adiciona os ids das posicoes da combinação escolhida a uma lista de posicoes
            for comb in lista_pc_comb:
                if (comb['id'] == pc_comb_atual):
                    lista_pc_ids_comb_esc = (comb['pos_comb'])
            #adiciona os ids das posicoes a um cadastro de preenchimento delas
            id_pos = 0
            for pos in lista_ocupa_pos_comb_atual:
                if (pos['ocupada'] == 0):
                    pos['id_pos'] = lista_pc_ids_comb_esc[id_pos]
                id_pos +=1
            #Verifica se o id da posicao escolhida está ocupado por ele mesmo 
            # caso esteja o retira das posicoes para jogar da combinação escolhida
            for pos in lista_ocupa_pos_comb_atual:
                for posicao in lista_todas_posicoes:
                    if (pos['id_pos'] == posicao['id']):
                        if (posicao['simbolo'] == 'O'):
                            pos['ocupada'] = 1
            #verifica os ids a jogar possiveis e aleatoriza um para jogar
            lista_id_alea_comb_jog = []
            for pos in lista_ocupa_pos_comb_atual:
                if (pos['ocupada'] == 0):
                    lista_id_alea_comb_jog.append(pos['id_pos'])
            if (lista_id_alea_comb_jog != []):
                pc_id_alea_comb_jog = random.choice(lista_id_alea_comb_jog)
            #verifica se combinação escolhida ainda é válida
            comb_valida = ''
            for id_pos in lista_pc_ids_comb_esc:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] == id_pos):
                        comb_valida += posicao['simbolo']
            #caso a combinação não possua uma posicao ocupada por si próprio
            # troca para o modo aleatório
            if (comb_valida not in ('O  ',' O ','  O','O O','OO ',' OO','   ')):
                pc_comb_atual = 0
            else:
                #altera o status ocupada do id da combinação a jogar
                # depois parte para preencher
                for pos in lista_ocupa_pos_comb_atual:
                    if (pos['id_pos'] == pc_id_alea_comb_jog):
                        pos['ocupada'] = 1
                        for posicao in lista_todas_posicoes:
                            if (posicao['id'] == pc_id_alea_comb_jog):
                                posicao['ocupada'] = 1
                                posicao['simbolo'] = 'O'
                break

#variáveis de jogadores
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]
#controles de jogada
ultima_jogada = [] #jogador ultima jogada, simbolo do jogador
primeira_jogada = True
#variaveis globais do computador
pc_comb_atual = 0
pc_id_alea_comb_jog = 0
lista_pc_pos_comb_esc = []
lista_pos_val_modo_alea = []
lista_comb_possiveis = []
#cadastro de combinações do computador
lista_pc_comb = [
    {'id':1,'comb':'','valido':0,'pos_comb':[1,2,3]},#pos_comb são os ids das posicoes
    {'id':2,'comb':'','valido':0,'pos_comb':[4,5,6]},
    {'id':3,'comb':'','valido':0,'pos_comb':[7,8,9]},
    {'id':4,'comb':'','valido':0,'pos_comb':[1,4,7]},
    {'id':5,'comb':'','valido':0,'pos_comb':[2,5,8]},
    {'id':6,'comb':'','valido':0,'pos_comb':[3,6,9]},
    {'id':7,'comb':'','valido':0,'pos_comb':[1,5,9]},
    {'id':8,'comb':'','valido':0,'pos_comb':[3,5,7]}]
#cadastro de posicoes
lista_todas_posicoes = [
    {'ocupada':1,'simbolo':'X','linha':1,'coluna':1,'id':1}, 
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':2,'id':2}, 
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':3,'id':3}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':1,'id':4}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':2,'id':5}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':3,'id':6}, 
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':1,'id':7}, 
    {'ocupada':1,'simbolo':'X','linha':3,'coluna':2,'id':8}, 
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':3,'id':9}]

def pc_comb():
    #limpa combinações possíveis anteriores
    for comb in lista_pc_comb:
        comb['comb'] = ''
        comb['valido'] = 0
    #verifica cada "pos_comb" de "lista_pc_comb" e atribui o simbolo
    # de cada id de posicao de "lista_todas_posicoes"
    for comb in lista_pc_comb:
        pos_comb = comb['pos_comb']
        for posicao in lista_todas_posicoes:
            if(posicao['id'] in pos_comb):
                comb['comb'] += posicao['simbolo']
    #computador considera primeiro as combinações que já ocupou
    #verifica combinações em que o PC já tenha ocupado duas posicões
    comb_ocup_dois = False
    for comb in lista_pc_comb:
        if(comb['comb'] in ('O O','OO ',' OO')):
            comb['valido'] = 1
            comb_ocup_dois = True
    #verifica combinações em que o PC já tenha ocupado uma posicão
    comb_ocup_um = False
    if (comb_ocup_dois == False):
        for comb in lista_pc_comb:
            if(comb['comb'] in ('O  ',' O ','  O')):
                comb['valido'] = 1
                comb_ocup_um = True
    #verifica combinações em que o PC não tenha ocupado posicão
    if (comb_ocup_um == False and comb_ocup_dois == False):
        for comb in lista_pc_comb:
            if(comb['comb'] in ('   ')):
                comb['valido'] = 1

def menu():
    print('JOGO DA VELHA 1.0\n Coluna x Linha\n')
    for id in range(1,10,1):
        if (id in (1,4,7)):
            print('    |', end='')
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id):
                print(posicao['simbolo'], end='')
                print('|', end='')
        if(id in (3,6)):
            print('\r')
    print('\n')

from os import system
import random
pc_comb()
print(lista_pc_comb)
menu()