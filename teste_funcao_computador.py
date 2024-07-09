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
    {'id':1,'comb':'','valido':0},{'id':2,'comb':'','valido':0},
    {'id':3,'comb':'','valido':0},{'id':4,'comb':'','valido':0},
    {'id':5,'comb':'','valido':0},{'id':6,'comb':'','valido':0},
    {'id':7,'comb':'','valido':0},{'id':8,'comb':'','valido':0},]

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
    menu = f'JOGO DA VELHA 1.0\n\n Coluna x Linha\n      1 2 3  \n    1|{lista_exibe_pos[0]}|{lista_exibe_pos[1]}|{lista_exibe_pos[2]}|\n    2|{lista_exibe_pos[3]}|{lista_exibe_pos[4]}|{lista_exibe_pos[5]}|\n    3|{lista_exibe_pos[6]}|{lista_exibe_pos[7]}|{lista_exibe_pos[8]}|\n'
    print(menu)

#from os import system
import random
from os import system

pc_comb_possiveis()

"""system('cls')
dificuldade = 1
turno_computador(dificuldade)
menu()"""