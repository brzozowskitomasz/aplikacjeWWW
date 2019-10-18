a_list = [0,3,4,2,1,5,6,8]
b_list = [3,4,5,3,7,8,6,5]

i = 0
def funkcja(a_list,b_list):
    lista_wynikowa = []

    for i,j in enumerate(a_list):
        if i%2==0:
            lista_wynikowa.append(i)
    for i,j in enumerate(b_list):
        if i%2 is not 0:
            lista_wynikowa.append(i)
    return lista_wynikowa
print(funkcja(a_list,b_list))