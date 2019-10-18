def funkcja(a_lista,b_lista):
    c_lista=[]
    for x in a_lista:
        if x%2==0:
            c_lista.append(x)
    for y in b_lista:
             if y%2>0:
                 c_lista.append(y)
    return c_lista

a_lista1=[1, 2, 3, 4, 5]
b_lista1=[11,12,13,14,15]

print(funkcja(a_lista1,b_lista1))
