def funkcja(data_text):
    slownik={}
    tab=[]
    slownik["dlugosc"]=len(data_text)
    for x in data_text:
        tab.append(x)
    slownik["lista"]=tab
    slownik["duze"]=data_text.upper()
    slownik["male"]=data_text.lower()
    return slownik

print(funkcja("Dog"))