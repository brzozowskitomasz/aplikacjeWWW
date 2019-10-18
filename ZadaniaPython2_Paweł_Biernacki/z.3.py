letter = 5
text = "5Ala5ma5Kota5"
def funkcja_usun(text,letter):
    for i in text:
        if i==letter:
            i = i.replace(i,"")

    return text
