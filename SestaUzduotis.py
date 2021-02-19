# Sesta

class sixth:
    def get_input(self):
            result = ""
            try:
                number = int(input("Įveskite skaičių: "))
            except: print("Įveskite skaičių!")
            if number == 0:
                exit()

            for i in range(1, number + 1):
                result += "{}".format(i)
                if i != number:
                    result += "+"
            result += " = {}".format(sum(range(number + 1)))
            self.show_results(result)

    def show_results(self, result):
        print("0+"+result)

si = sixth()
si.get_input()