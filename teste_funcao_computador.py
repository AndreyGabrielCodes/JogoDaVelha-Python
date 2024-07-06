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
    #verifica posicoes validas
    lista_posicoes_validas = []
    lista_posicoes_validas.clear()
    for posicao in lista_todas_posicoes:
        if(posicao['ocupada'] == 0):
                lista_posicoes_validas.append(posicao['id'])
    match dificuldade:
        case 1: #facil
            posicao_escolhida = 0
            posicao_escolhida = random.choice(lista_todas_posicoes)
            for posicao in lista_todas_posicoes:
                if (posicao['id'] == posicao_escolhida):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = 'O'
        case 2: #medio
            print
        case 3: # dificil 
            print

lista_todas_posicoes = [{'ocupada':0,'simbolo':' ','linha':1,'coluna':1,'id':1}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':2,'id':2}, 
                        {'ocupada':0,'simbolo':' ','linha':1,'coluna':3,'id':3}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':1,'id':4}, 
                        {'ocupada':1,'simbolo':' ','linha':2,'coluna':2,'id':5}, 
                        {'ocupada':0,'simbolo':' ','linha':2,'coluna':3,'id':6}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':1,'id':7}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':2,'id':8}, 
                        {'ocupada':0,'simbolo':' ','linha':3,'coluna':3,'id':9}]

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
    menu = f"""JOGO DA VELHA 1.0\n\n Coluna x Linha\n      1 2 3  \n    1|{posicao1_1}|{posicao1_2}|{posicao1_3}|\n    2|{posicao2_1}|{posicao2_2}|{posicao2_3}|\n    3|{posicao3_1}|{posicao3_2}|{posicao3_3}|\n"""
    print(menu)

#from os import system
import random

print(menu)
dificuldade = 1
turno_computador(dificuldade)
print(menu)