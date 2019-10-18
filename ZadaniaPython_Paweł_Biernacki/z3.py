# Zad.3

test = "test"

print(test)
#wyrownanie do prawej
print("{:>10}".format(test))
#obcinanie za dlugich wyrazow
print("{:.2}".format (test))
# 8 znakow przed i 4 po przecinku
print("{: 08.4f}".format( 2.141596753777789793 ))
#liczby dodatnie rowniez sa poprzedzone znakiem
print("{:+d}".format ( 42 ))

#Użyj znaku spacji, aby wskazać, że liczby ujemne powinny być poprzedzone symbolem minus,
# a spacja wiodąca powinna być użyta dla liczb dodatnich.
print("{: d}".format(( -  23 )))
