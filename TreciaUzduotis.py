# Trecia

class third:
    def get_input(self):
        try:
            integer = int(input("Įveskite skaičių:"))
            list_length = int(input("Įveskite sąrašo ilgį:"))
            list_of_numbers=[]
            for i in range(0, list_length):
                list_element = int(input())
                list_of_numbers.append(list_element)
            self.list_calculations(integer, list_of_numbers)
        except: print("Įveskite skaičių!")

    def list_calculations(self, integer, list_of_numbers):
        try:
            maxi=max(list_of_numbers)
            mini=min(list_of_numbers)
            sum_of_numbers=sum(list_of_numbers)
            average=sum_of_numbers/len(list_of_numbers)
            numbers_greater_list = [i for i in list_of_numbers if i > integer]
            numbers_lower_list = [i for i in list_of_numbers if i < integer]
            self.show_results(maxi, mini, average, numbers_greater_list, numbers_lower_list)
        except: print("Bandykite iš naujo!")

    def show_results (self, maxi, mini, average, numbers_greater_list, numbers_lower_list):
        print("Sąrašo vidurkis: "+str(average))
        print("Sąrašo didžiausias skaičius: "+str(maxi))
        print("Sąrašo mažiausias skaičius: " + str(mini))
        print("Sąrašo skaičių skaičius didesnis už įvestą: "+str(len(numbers_greater_list)))
        print("Sąrašo skaičių skaičius mažesnis už įvestą: " + str(len(numbers_lower_list)))

t=third()
t.get_input()