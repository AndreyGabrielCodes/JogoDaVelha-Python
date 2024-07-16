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

def pc_pos_alea():
    #lista todas as posições disponíveis para o modo jogar
    lista_pos_val_modo_facil.clear()
    for posicao in lista_todas_posicoes:
        if(posicao['ocupada'] == 0):
                lista_pos_val_modo_facil.append(posicao['id'])
    #escolhe aleatoriamente uma das posições e joga
    posicao_escolhida = 0
    posicao_escolhida = random.choice(lista_pos_val_modo_facil)
    for posicao in lista_todas_posicoes:
        if (posicao['id'] == posicao_escolhida):
            posicao['ocupada'] = 1
            posicao['simbolo'] = 'O'

def pc_turno():

    #criar verificação dupla que verifica se o jogador pode ganhar em casos onde 
    # ao tentar bloquear uma combinação a outra vence
    # fazer com que o computador responda forçando o jogador a bloqueá-lo

    while(True):
        global pc_comb_valida
        global id_aleatorio_comp_jog
        global pc_comb_escolhida
        #cadastro de preenchimento das posições da combinação escolhida pelo computador
        lista_preenc_pos_comb_esc = [
            {'id':1,'pos':0,'ocupada':0},
            {'id':2,'pos':0,'ocupada':0},
            {'id':3,'pos':0,'ocupada':0}]
        lista_comb_possiveis.clear()
        pc_comb()
        #gera combinações possíveis
        for comb in lista_pc_comb:
            if (comb['valido'] == 1):
                lista_comb_possiveis.append(comb['id'])
        #caso todas as combinações estejam indisponíveis
        # altera para o computador jogador aleatoriamente
        if (lista_comb_possiveis == []):
            pc_comb_escolhida = 0
            pc_pos_alea()
            break
        else:
            #caso o computador já tenha escolhido uma combinação
            # não é aleatorizado uma nova
            if (pc_comb_escolhida == 0):
                pc_comb_escolhida = random.choice(lista_comb_possiveis)
        
        if ((pc_comb_escolhida != 0)):
            #adiciona os ids das posicoes da combinação escolhida a uma lista de posicoes
            for comb in lista_pc_comb:
                if (comb['id'] == pc_comb_escolhida):
                    lista_pc_pos_comb_esc = (comb['pos_comb'])
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
                # troca para o modo aleatório
            if (comb_valida not in ('O  ',' O ','  O','O O','OO ',' OO','   ')):
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

def pc_modo_dificil():
    id_jog_usu = [] #recebe até 3 jogadas
    num_jog_usu = 0

    #insere o id das posicoes das 3 primeiras jogadas do jogador
    for posicao in lista_todas_posicoes:
        if((posicao['ocupada'] == 1) and (posicao['simbolo'] == 'X')):
            num_jog_usu += 1
            if(num_jog_usu < 3):
                id_jog_usu.append(posicao['id'])

def pc_comb():
    #limpa combinações possíveis anteriores
    for comb in lista_pc_comb:
        comb['comb'] = ''
        comb['valido'] = 0
    #verifica cada "pos_comb" de "lista_pc_comb" e atribui o simbolo
    # de cada id de posicao de "lista_todas_posicoes"
    for pc_comb in lista_pc_comb:
        comb_atual = ''
        comb_atual = pc_comb['pos_comb']
        id_comb_atual = pc_comb['id']
        for posicao in lista_todas_posicoes:
            if(posicao['id'] in comb_atual):
                for pc_comb in lista_pc_comb:
                    if(pc_comb['id'] == id_comb_atual):
                        pc_comb['comb'] += posicao['simbolo']
    
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

def status_partida():
    status = 0 #status: 0 - jogo acontecendo | 1 - empate | 2 - vitória
    comb_pos = [
        [1,2,3],[4,5,6],[7,8,9],#verifica linhas
        [1,4,7],[2,5,8],[3,6,9],#verifica colunas
        [1,5,9],[3,5,7],        #verifica diagonais
        [1,2,3,4,5,6,7,8,9]]    #verifica todas as posicoes
    for comb in comb_pos:
        comb_ocup = 0
        comb_feita = ''
        for posicao in lista_todas_posicoes:
            if(posicao['id'] in comb and posicao['simbolo'] in ('X','O')):
                comb_feita += posicao['simbolo']
                comb_ocup += 1
        if (comb_feita == 'XXX'):
            jogador_x[3] = 1
            status = 2
            return status
        elif(comb_feita == 'OOO'):
            jogador_o[3] = 1
            status = 2
            return status
        elif(comb_ocup == 9):
            status = 1
            return status
    return status 

def escolhe_posicao():
   valido = False
   #repete a escolha das posicoes conforme retorno true ou false da função "atribui_posicao"
   while(valido == False):
        coluna_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma coluna: ',int,1,3)
        linha_escolhida = valida_per(f'{jog_ult_jogada}, escolha uma linha: ',int,1,3)
        valido = False
        posicao_ocupada = 0
        for posicao in lista_todas_posicoes:
            if ((posicao['linha'] == linha_escolhida) and (posicao['coluna'] == coluna_escolhida)):
                posicao_ocupada = posicao['ocupada']
        if (posicao_ocupada == 1):
            system('cls')
            menu()
            print('*Posição escolhida está ocupada! Tente novamente\n')
            valido = False
        else:
            for posicao in lista_todas_posicoes:
                if ((posicao['linha'] == linha_escolhida) and (posicao['coluna'] == coluna_escolhida)):
                    posicao['ocupada'] = 1
                    posicao['simbolo'] = simbolo_ult_jog
            valido = True

def turno_atual(modo_jogo,inicio_partida):
    global jogador_x
    global jogador_o
    global jog_ult_jogada
    global simbolo_ult_jog
    global primeira_jogada
    if (inicio_partida):
        if (modo_jogo == 1):
            #aleatoriza o jogador que inicia a partida
            jogadores = [jogador_x[1],jogador_o[1]]
            simbolos_jogadores = [jogador_x[2],jogador_o[2]]
            aleatorio = random.randint(0,1)
            jog_ult_jogada = jogadores[aleatorio]
            simbolo_ult_jog = simbolos_jogadores[aleatorio]
        else:
            jog_ult_jogada = jogador_x[1]
            simbolo_ult_jog = 'X'
        input(f'{jog_ult_jogada} inicia a partida!\n\nEnter para iniciar partida')
    else:
        if (primeira_jogada):
            escolhe_posicao()
            primeira_jogada = False
        #modo jogador x jogador - altera o jogador conforme o ultimo que jogou
        elif ((jog_ult_jogada == jogador_x[1])):
            jog_ult_jogada = jogador_o[1]
            simbolo_ult_jog = jogador_o[2]
            #modo jogador x computador - altera o jogador conforme modo
            if (modo_jogo == 1):
                escolhe_posicao()
            else:
                pc_turno()
        else:
            jog_ult_jogada = jogador_x[1]
            simbolo_ult_jog = jogador_x[2]
            escolhe_posicao()

def reseta_partida():
    global pc_comb_escolhida
    global pc_comb_valida
    global id_aleatorio_comp_jog
    global primeira_jogada
    #reseta status de witoria dos jogadores
    jogador_x[3] = 0
    jogador_o[3] = 0
    #reseta todas as posicoes para valores padrão
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

def menu_final_jogo():
    jogador_vencedor = ''
    pontos_jogador_vencedor = 0
    dif_empate = False
    system('cls')
    if (jogador_x[0] > jogador_o[0]):
        jogador_vencedor = jogador_x[1]
        pontos_jogador_vencedor = jogador_x[0]
        dif_empate = True
    elif (jogador_o[0] > jogador_x[0]):
        jogador_vencedor = jogador_o[1]
        pontos_jogador_vencedor = jogador_o[0]
        dif_empate = True
    else:
        print(f'Partida de Jogo da Velha não teve vencedores!\n')
        print(f'Total de pontos feitos de {jogador_x[1]}: {jogador_x[0]} pontos')
        print(f'Total de pontos feitos de {jogador_o[1]}: {jogador_o[0]} pontos\n')
    if (dif_empate):
        system('cls')
        print(f'Parabéns {jogador_vencedor}!!!\n')
        print(f'Partida de Jogo da Velha foi vencida por {jogador_vencedor}!\n')
        print(f'Total de pontos feitos: {pontos_jogador_vencedor} pontos\n')
    
def menu_final_rodada():
    global jogador_x
    global jogador_o
    resultado = ''
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

def menu():
    id_posicao = 1
    lista_exibe_pos = []
    for i in range(1,11,1):
        for posicao in lista_todas_posicoes:
            if (posicao['id'] == id_posicao):
                lista_exibe_pos.append(posicao['simbolo'])
        id_posicao += 1
    print('JOGO DA VELHA 1.0\n Coluna x Linha\n')
    quebra_linha = 0
    for simbolo in lista_exibe_pos:
        if(quebra_linha == 3):
            quebra_linha = 0
            print('\r')
        if(quebra_linha == 0):
            print('    |', end='')
        print(f'{simbolo}|', end='')
        quebra_linha += 1
    print('\n')
    
def main():
    #programa principal
    system('cls')
    print('|        JOGO DA VELHA        |')
    print('|                             |')
    print('|        MODOS DE JOGO        |')
    print('| 1 - Jogador x Jogador       |')
    print('| 2 - Jogador x Computador    |\n')
    modo_jogo = valida_per('Escolha um modo de jogo: ','menu',1,2)
    match modo_jogo:
        case 1:
            jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
            jogador_o[1] = valida_per('| Nome do Jogador que será o O: ',str)
        case 2:
            jogador_x[1] = valida_per('\n| Nome do Jogador que será o X: ',str)
            jogador_o[1] = 'Computador'
    while(True):
        system('cls')
        turno_atual(modo_jogo,True)
        #estrutura de repetição da jogada
        while(status_partida() == 0): #repetirá enquanto a partida estiver com status de jogo acontecendo
            system('cls')
            menu()
            turno_atual(modo_jogo,False)
        #estrutura após a finalização da partida
        menu_final_rodada()
        resetar_partida = valida_per('\nDeseja iniciar uma nova partida ? (1/0): ','menu',0,1)
        if(resetar_partida == 1):
            reseta_partida()
            continue
        else:
            menu_final_jogo()
            break

#variáveis de jogadores
jogador_x = [0,'','X',0] #pontuação, nome, simbolo, vitoria (0 e 1)
jogador_o = [0,'','O',0]
#controles de jogada
jog_ult_jogada = ''
simbolo_ult_jog = ''
primeira_jogada = True
#variaveis globais do computador
pc_comb_escolhida = 0
pc_comb_valida = False
lista_pc_pos_comb_esc = []
id_aleatorio_comp_jog = 0
lista_pos_val_modo_facil = []
dificuldade_computador = 1
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
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':1,'id':1}, 
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':2,'id':2}, 
    {'ocupada':0,'simbolo':' ','linha':1,'coluna':3,'id':3}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':1,'id':4}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':2,'id':5}, 
    {'ocupada':0,'simbolo':' ','linha':2,'coluna':3,'id':6}, 
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':1,'id':7}, 
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':2,'id':8}, 
    {'ocupada':0,'simbolo':' ','linha':3,'coluna':3,'id':9}]

from os import system
import random

main()