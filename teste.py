lista_todas_posicoes = [
    {'simbolo':'X','linha':1,'coluna':1,'id':1}, {'simbolo':' ','linha':1,'coluna':2,'id':2}, 
    {'simbolo':' ','linha':1,'coluna':3,'id':3}, {'simbolo':' ','linha':2,'coluna':1,'id':4}, 
    {'simbolo':' ','linha':2,'coluna':2,'id':5}, {'simbolo':' ','linha':2,'coluna':3,'id':6}, 
    {'simbolo':' ','linha':3,'coluna':1,'id':7}, {'simbolo':' ','linha':3,'coluna':2,'id':8}, 
    {'simbolo':' ','linha':3,'coluna':3,'id':9}]

lista_todas_comb = []
for pos in lista_todas_posicoes:
    if (pos['simbolo'] == 'X'):
        lista_duas_pos = []
        lista_duas_pos_invert = []
        for i in range(1,10,1):
            if (pos['id'] != i):
                lista_duas_pos = [pos['id'],i]
                lista_duas_pos_invert = [i,pos['id']]
                lista_todas_comb.append(lista_duas_pos)
                lista_todas_comb.append(lista_duas_pos_invert)

print(lista_todas_comb)