#variavel_x_y - X é linha e Y é coluna

#controle de posição
    #indice 0 é para ocupação da posição quando igual a 1
    #indice 1 é para preenchimento do simbolo inserido
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

#teste
posicao_1_1[0] = 1
posicao_1_1[1] = 'X'

print(posicao_1_1[:])