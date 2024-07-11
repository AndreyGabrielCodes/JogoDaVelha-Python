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

def pc_modo_facil():
    pc_pos_valida()
    posicao_escolhida = 0
    posicao_escolhida = random.choice(lista_pos_val_modo_facil)
    for posicao in lista_todas_posicoes:
        if (posicao['id'] == posicao_escolhida):
            posicao['ocupada'] = 1
            posicao['simbolo'] = 'O'

def pc_modo_medio(dificuldade):
    while(True):
        global pc_comb_escolhida
        global pc_comb_valida
        global dificuldade_computador
        global id_aleatorio_comp_jog
        global pc_comb_escolhida
        lista_comb_possiveis.clear()
        pc_comb_possiveis()
        #gera combinações possíveis
        for comb in lista_pc_comb:
            if (comb['valido'] == 1):
                lista_comb_possiveis.append(comb['id'])
        #caso todas as combinações estejam indisponíveis
        # altera para o computador jogador aleatoriamente
        if (lista_comb_possiveis == []):
            pc_comb_escolhida = 0
            pc_modo_facil()
            break
        else:
            #caso o computador já tenha escolhido uma combinação
            # não é aleatorizado uma nova
            if (pc_comb_escolhida != 0):
                pc_comb_valida = True
            #caso não haja combinação escolhida gera uma nova
            else:
                pc_comb_escolhida = random.choice(lista_comb_possiveis)
                pc_comb_valida = True
        
        if ((pc_comb_valida == True)):
            #adiciona os ids das posicoes da combinação escolhida a uma lista de posicoes
            for comb in lista_pc_comb:
                if (comb['id'] == pc_comb_escolhida):
                    lista_pc_pos_comb_esc = (comb['pos_comb'])
            #limpa a ocupação das posicoes da combinação escolhida pelo computador
            for resetar in lista_preenc_pos_comb_esc:
                resetar['pos'] = 0
                resetar['ocupada'] = 0
            #adiciona os ids das posicoes a um cadastro de preenchimento delas
            x = 0
            for lista in lista_preenc_pos_comb_esc:
                if (lista['ocupada'] == 0):
                    lista['pos'] = lista_pc_pos_comb_esc[x]
                x +=1
            #Verifica se o id da posicao escolhida está ocupado por ele mesmo 
            # caso esteja o retira das posicoes para jogar da combinação escolhida
            for lista in lista_preenc_pos_comb_esc:
                for posicao in lista_todas_posicoes:
                    if (lista['pos'] == posicao['id']):
                        if (posicao['simbolo'] == 'O'):
                            lista['ocupada'] = 1
            #verifica os ids a jogar possiveis e aleatoriza um para jogar
            lista_id_aleatorio = []
            for lista in lista_preenc_pos_comb_esc:
                if (lista['ocupada'] == 0):
                    lista_id_aleatorio.append(lista['pos'])
            if (lista_id_aleatorio != []):
                id_aleatorio_comp_jog = random.choice(lista_id_aleatorio)
            #verifica se combinação escolhida ainda é válida
            comb_valida = ''
            for id_pos in lista_pc_pos_comb_esc:
                for posicao in lista_todas_posicoes:
                    if (posicao['id'] == id_pos):
                        comb_valida += posicao['simbolo']
                #caso a combinação não possua uma posicao ocupada por si próprio
                # troca de modo médio para o facil
            if (comb_valida not in ('O  ',' O ','  O','O O','OO ',' OO','   ')):
                pc_comb_valida = False
                pc_comb_escolhida = 0
                lista_comb_possiveis.clear()
            else:
                #altera o status ocupada do id da combinação a jogar
                # depois parte para preencher
                for ocupar in lista_preenc_pos_comb_esc:
                    if (ocupar['pos'] == id_aleatorio_comp_jog):
                        ocupar['ocupada'] = 1
                        for posicao in lista_todas_posicoes:
                            if (posicao['id'] == id_aleatorio_comp_jog):
                                posicao['ocupada'] = 1
                                posicao['simbolo'] = 'O'
                break

def pc_pos_valida():
    lista_pos_val_modo_facil.clear()
    for posicao in lista_todas_posicoes:
        if(posicao['ocupada'] == 0):
                lista_pos_val_modo_facil.append(posicao['id'])

def pc_comb_possiveis():
    #verifica todas as combinações possives e as retorna na lista "lista_pc_comb"
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
            if(comb['comb'] in ('O  ',' O ','  O','O O','OO ',' OO','   ')):
            #if(comb['comb'] == '   '):
                comb['valido'] = 1
        numero_combinacao +=1

def turno_computador(dificuldade):
    """
    Primeiro o computador verifica se o jogador oponente falta uma posicao para fechar uma combinação de vitória
     e o tenta barrar
    Caso não, verifica combinações possíveis, escolhe uma, e começa a completá-la
    Dificuldades:
    1 - Facil - Joga em posicoes aleatórias
    2 - Medio - Joga para formar combinações
    3 - Dificil - Joga tentando bloquear o jogador e forçando empate
    """
    #verifica posicoes validas para o computador trabalhar em cima
    
    match dificuldade:
        case 1: #facil
            pc_modo_facil()
        case 2: #medio
            pc_modo_medio(dificuldade)
        case 3: # dificil 
            print

def reseta_partida():
    global pc_comb_escolhida
    global pc_comb_valida
    global id_aleatorio_comp_jog
    global primeira_jogada
    #reseta status de witoria dos jogadores
    jogador_x[3] = 0
    jogador_o[3] = 0
    #reseta posicoes para valores padrão
    for posicao in lista_todas_posicoes:
        if (posicao['ocupada'] == 1):
            posicao['ocupada'] = 0
            posicao['simbolo'] = ' '
    #reseta variavel padrão de inicio de jogo
    primeira_jogada = True
    #resetar variaveis de controle do computador
    pc_comb_escolhida = 0
    pc_comb_valida = False
    lista_pc_pos_comb_esc.clear()
    id_aleatorio_comp_jog = 0
    lista_pos_val_modo_facil.clear()
    #limpa a ocupação das posicoes da combinação
    # escolhida pelo computador
    for resetar in lista_preenc_pos_comb_esc:
        resetar['pos'] = 0
        resetar['ocupada'] = 0

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
    else:
        if ((jog_ult_jogada == jogador_x[1])):
            jog_ult_jogada = jogador_o[1]
            simbolo_ult_jog = jogador_o[2]
            #modo jogador x computador - altera o jogador conforme modo
            if (modo_jogo == 1):
                escolhe_posicao()
            else:
                turno_computador(dificuldade_computador)
        else:
            jog_ult_jogada = jogador_x[1]
            simbolo_ult_jog = jogador_x[2]
            escolhe_posicao()

def escolhe_posicao():
   repete_escolha = False
   #repete a escolha das posicoes conforme retorno true ou false da função "atribui_posicao"
   while(repete_escolha == False):
        coluna_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma coluna: ',int,1,3)
        linha_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma linha: ',int,1,3)
        repete_escolha = atribui_posicao(linha_escolhida, coluna_escolhida, simbolo_ult_jog) 

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
    
#variaveis globais do computador
pc_comb_escolhida = 0
pc_comb_valida = False
lista_pc_pos_comb_esc = []
id_aleatorio_comp_jog = 0
lista_pos_val_modo_facil = []
dificuldade_computador = 1
lista_comb_possiveis = []
#cadastro de preenchimento das posições da combinação escolhida pelo computador
lista_preenc_pos_comb_esc = [
    {'id':1,'pos':0,'ocupada':0},
    {'id':2,'pos':0,'ocupada':0},
    {'id':3,'pos':0,'ocupada':0}]
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
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':1,'id':1}, 
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
        else:
            resultado = (f'Vitoria de {jogador_o[1]} que escolheu {jogador_o[2]}!')
            jogador_o[0] += 1
    print(f'| Resultado da partida: {resultado}\n')
    print(f'| Pontuações:\n| - {jogador_x[1]}: {jogador_x[0]}\n| - {jogador_o[1]}: {jogador_o[0]}')
    resetar_partida = valida_per('\nDeseja iniciar uma nova partida ? (1/0): ','menu',0,1)
    if(resetar_partida == 1):
        reseta_partida()
        continue
    else:
        break
system('cls')
print('Jogo finalizado, obrigado por jogar !')