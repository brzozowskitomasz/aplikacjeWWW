
lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy" \
              " wypełniacz w przemyśle poligraficznym. Został po raz pierwszy " \
              "użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
              " Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie " \
              "niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, " \
              "zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum " \
              "oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"


imie = "Paweł"
nazwisko = "Biernacki"
litera_1 = imie[2]
litera_2 = nazwisko[3]
j=0
k=0
for i in lorem_ipsum:
    if i == litera_1:
        j+=1
    if i == litera_2:
        k+=1
print(j,k)
print('W tekście jest {} liter {} oraz {} liter {}'.format(k,litera_1,j,litera_2))

# Zadanie 3