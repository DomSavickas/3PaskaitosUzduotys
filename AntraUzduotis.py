# Antra

class second:
    def get_input(self):
        #try:
            height = int(input("Įveskite savo ūgį:"))
            weight = int(input("Įveskite savo svorį:"))
            self.BMI_calculation(height, weight)
        #except: print("Įveskite skaičių!")

    def BMI_calculation(self, height, weight):
        try:
            BMI=round(weight/height**2*10000,2)
            if BMI > 25:
                verdict="Jūs turite antsvorį"
            elif BMI< 18.5:
                verdict="Jūsų svoris yra per mažas "
            else:
                verdict="Jūsų BMI yra sveikas"
        except: print("Bandykite iš naujo!")
        self.show_results(BMI, verdict)

    def show_results (self, BMI, verdict):
        print("Jūsų BMI: "+str(BMI)+", tai reiškia: "+str(verdict))

s=second()
s.get_input()