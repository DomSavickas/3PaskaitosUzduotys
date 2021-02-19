# Penkta

class fifth:
    def get_input(self):
        #try:
            sequence = input("Įveskite kableliais atskirtą skaičių seką:")

            self.generator(sequence)
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

fif=fifth()
fif.get_input()