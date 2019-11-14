
def temperatura(celsjusz, naCoZamienic):
    if naCoZamienic == 'f':
        return 32+1.8*celsjusz
    if naCoZamienic == 'r':
        return (celsjusz + 273.15)*1.8
    if naCoZamienic == 'k':
        return celsjusz + 273.15


x = int(input("Podaj ile stopni celsjusza:"))
y = input("Na co zamienić? \n"
                     "f: zamien na fahrenheita \n"
                     "r: zamien na rankine'a \n"
                     "k: zamien na kelwina \n")
print(temperatura(x,y))