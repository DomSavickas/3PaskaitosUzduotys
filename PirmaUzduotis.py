# Pirma
import math
class first:
    def get_input(self):
        try:
            a = int(input("Įveskite pirmają kraštinę prie stataus kampo: "))
            b = int(input("Įveskite antrają kraštinę prie stataus kampo: "))
            self.theorem_calculation(a, b)
        except: print("Įveskite skaičių!")
    def theorem_calculation(self, a, b):
        square_sum_of_ab=a**2+b**2
        hypotenuse_length=math.sqrt(square_sum_of_ab)
        try:
            validation=round(hypotenuse_length**2)
            if validation == square_sum_of_ab:
                print("Rezultatas geras")
                self.show_result(hypotenuse_length)
        except: print("Rezultatas netinkamas")
    def show_result (self, hypotenuse_length):
        print("Įžambinės kraštinės ilgis yra: "+str(round(hypotenuse_length, 2)))

f=first()
f.get_input()