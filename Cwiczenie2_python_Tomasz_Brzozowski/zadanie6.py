class calculator:

    def add(self, liczba1, liczba2):
        liczba3 = liczba1 + liczba2
        return liczba3

    def difference(self, liczba1, liczba2):
        liczba3 = liczba1 - liczba2
        return liczba3

    def multiply(self, liczba1, liczba2):
        liczba3 = liczba1 * liczba2
        return liczba3

    def divide(self, liczba1, liczba2):
        liczba3 = liczba1 / liczba2
        return liczba3


class ScienceCalculator(calculator):
    def pot(self, liczba1, liczba2):
        liczba3 = liczba1 ** liczba2
        return liczba3


obiekt = calculator()
print(obiekt.add(1, 2))
print(obiekt.difference(1, 2))
print(obiekt.multiply(1, 2))
print(obiekt.divide(1, 2))
obiekt1 = ScienceCalculator()
obiekt1.add(1, 2)
print(obiekt1.pot(2,3))
