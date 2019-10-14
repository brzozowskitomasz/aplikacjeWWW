zmienna1="Ktos"
zmienna2="Ktokolwiek"
litera1="o"
litera2="k"
liczba_liter1=0
liczba_liter2=0
for x in range(len(zmienna1)):
 if zmienna1[x]==litera1:
   liczba_liter1+=1

for y in range(len(zmienna2)):
 if zmienna2[y]==litera2:
   liczba_liter2+=1

print("W", zmienna1 ,"liczba liter",litera1,"jest",liczba_liter1)
print("W", zmienna2 ,"liczba liter",litera2,"jest",liczba_liter2)