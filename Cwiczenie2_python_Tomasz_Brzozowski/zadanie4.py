def funkcja(wartosc,temperature_type):
    if temperature_type=="far":
        wartosc=(wartosc*1.8)+32
    if temperature_type=="ran":
        wartosc=(wartosc+273.15)*1.8
    if temperature_type == "kelvin":
        wartosc = wartosc + 273.15

    return wartosc

print(funkcja(5,"far"))
print(funkcja(5,"ran"))
print(funkcja(5,"kelvin"))
