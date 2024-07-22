id_pri_pos_jog = 6
id_ret = 0
lista_pri_id_jog = [{'pos':[1,3,7,9],'ret':5},{'pos':[4,5,8],'ret':7},{'pos':[2],'ret':3},{'pos':[6],'ret':9},]

for ids in lista_pri_id_jog:
    if (id_pri_pos_jog in ids['pos']):
        id_ret = ids['ret']
print(id_ret)

if (id_pri_pos_jog in (1,3,7,9)):
            id_ret_pri_pos = 5
        elif (id_pri_pos_jog in (4,5,8)):
            id_ret_pri_pos = 7
        elif (id_pri_pos_jog == 2):
            id_ret_pri_pos = 3
        else:
            id_ret_pri_pos = 9