pc_comb_escolhida = 0
pc_comb_valida = False
list_pc_pos_comb_esc = []
id_aleatorio_comp_jog = 0
lista_preenc_pos_comb_esc = [{'id':1,'pos':0,'ocupada':0},
                            {'id':2,'pos':0,'ocupada':0},
                            {'id':3,'pos':0,'ocupada':0}]

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
            pc_comb_possiveis()
            global pc_comb_escolhida
            global pc_comb_valida
            global dificuldade_computador
            global id_aleatorio_comp_jog
            global pos1
            global pos2
            global pos3
            lista_comb_possiveis = []
            #escolhe uma combinação aleatória caso nenhuma outra tenha sido escolhida
            if ((pc_comb_escolhida == 0) or (pc_comb_valida == False)):
                for comb in lista_pc_comb:
                    if (comb['valido'] == 1):
                        lista_comb_possiveis.append(comb['id'])
                #caso todas as combinações estejam indisponíveis
                # altera para o computador jogador aleatoriamente
                if (lista_comb_possiveis == []):
                    dificuldade_computador = 1
                else:
                    pc_comb_escolhida = 0
                    pc_comb_escolhida = random.choice(lista_comb_possiveis)
                    pc_comb_valida = True
            """
            #verificar se computador vai acabar vendo a própria combinação a ser feita e escolhendo outra
            else:
                #verifica se combinação escolhida ainda é válida
                for comb in lista_pc_comb:
                    if (comb['id'] == pc_comb_escolhida):
                        if (comb['valido'] == 0):
                            pc_comb_valida = False
                        else:
                            pc_comb_valida = True
            """
            
            if ((pc_comb_valida == True) and (dificuldade != 1)):
                lista_id_aleatorio = []
                #adiciona os ids das posicoes da combinação escolhida a uma lista de posicoes
                for comb in lista_pc_comb:
                    if (comb['id'] == pc_comb_escolhida):
                        list_pc_pos_comb_esc = (comb['pos_comb'])
                #adiciona os ids das posicoes a um cadastro de preenchimento delas
                x = 0
                for lista in lista_preenc_pos_comb_esc:
                    if (lista['ocupada'] == 0):
                        lista['pos'] = list_pc_pos_comb_esc[x]
                    x +=1
                #verifica os ids a jogar possiveis e aleatoriza um para jogar
                for lista in lista_preenc_pos_comb_esc:
                    if (lista['ocupada'] == 0):
                        lista_id_aleatorio.append(lista['pos'])
                id_aleatorio_comp_jog = random.choice(lista_id_aleatorio)
                #altera o status ocupada do id da combinação a jogar
                # depois parte para preencher
                for ocupar in lista_preenc_pos_comb_esc:
                    if (ocupar['pos'] == id_aleatorio_comp_jog):
                        ocupar['ocupada'] = 1
                        for posicao in lista_todas_posicoes:
                            if (posicao['id'] == id_aleatorio_comp_jog):
                                posicao['ocupada'] = 1
                                posicao['simbolo'] = 'O'
                        
        case 3: # dificil 
            print

def pc_comb_possiveis():
    numero_combinacao = 1
    #limpa combinações armazenadas
    for comb in lista_pc_comb:
        comb['comb'] = ''
        comb['valido'] = 0
    #verifica combinações e as armezena em cada id de combinação
    # para depois verificar quais podem ser feitas
    while(True):
        match numero_combinacao:
            #verifica linhas
            case 1:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (1,2,3)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 1):
                                comb['comb'] += posicao['simbolo']
            case 2:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (4,5,6)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 2):
                                comb['comb'] += posicao['simbolo']
            case 3:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (7,8,9)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 3):
                                comb['comb'] += posicao['simbolo']
            #verifica colunas
            case 4:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (1,4,7)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 4):
                                comb['comb'] += posicao['simbolo']
            case 5:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (2,5,8)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 5):
                                comb['comb'] += posicao['simbolo']
            case 6:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (3,6,9)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 6):
                                comb['comb'] += posicao['simbolo']
            #verifica diagonais
            case 7:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (1,5,9)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 7):
                                comb['comb'] += posicao['simbolo']
            case 8:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] in (3,5,7)):
                        for comb in lista_pc_comb:
                            if(comb['id'] == 8):
                                comb['comb'] += posicao['simbolo']
            case 10:
                break
        for comb in lista_pc_comb:
            if(comb['comb'] == '   '):
                comb['valido'] = 1
        numero_combinacao +=1
        
lista_pc_comb = [
    {'id':1,'comb':'','valido':0,'pos_comb':[1,2,3]},
    {'id':2,'comb':'','valido':0,'pos_comb':[4,5,6]},
    {'id':3,'comb':'','valido':0,'pos_comb':[7,8,9]},
    {'id':4,'comb':'','valido':0,'pos_comb':[1,4,7]},
    {'id':5,'comb':'','valido':0,'pos_comb':[2,5,8]},
    {'id':6,'comb':'','valido':0,'pos_comb':[3,6,9]},
    {'id':7,'comb':'','valido':0,'pos_comb':[1,5,9]},
    {'id':8,'comb':'','valido':0,'pos_comb':[3,5,7]}]

lista_todas_posicoes = [
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':1,'id':1},
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':2,'id':2},
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':3,'id':3},
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':1,'id':4},
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':2,'id':5},
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':3,'id':6},
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':1,'id':7},
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':2,'id':8},
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':3,'id':9}]

def menu():
    menu = ''
    id_posicao = 1
    lista_exibe_pos = []
    while(id_posicao < 10):
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id_posicao):
                lista_exibe_pos.append(posicao['simbolo'])
        id_posicao += 1
    menu = f'    1|{lista_exibe_pos[0]}|{lista_exibe_pos[1]}|{lista_exibe_pos[2]}|\n    2|{lista_exibe_pos[3]}|{lista_exibe_pos[4]}|{lista_exibe_pos[5]}|\n    3|{lista_exibe_pos[6]}|{lista_exibe_pos[7]}|{lista_exibe_pos[8]}|\n'
    print(menu)

#from os import system
import random
from os import system

dificuldade_computador = 2
x = 0
system('cls')
while(x < 3):
    turno_computador(dificuldade_computador)
    menu()
    x += 1