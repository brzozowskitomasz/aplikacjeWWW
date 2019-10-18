def funkcja(text,letter):
    a=0
    for x in text:
        if x==letter:
            a+=1

    return a

print(funkcja("Dogo","o"))