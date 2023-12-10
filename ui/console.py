from termcolor import colored

def printMeniu():
    """
    Afisam meniul
    """
    print("Va rugam sa alegeti o optiune de mai jos: ")
    print("   1) adaugati un zbor;")
    print("   2) stergeti un zbor dupa cod;")
    print("   3) vizualizati toate zborurile dupa orasul destinatie; ")
    print("   4) modificati zborurile cu o durata data;")
    print("   0) iesiti din aplicatie. ")

class Console:
    def __init__(self, srv):
        """
        Initializam consola pentru a lucra cu controllerul GRASP
        :param srv: service-ul zborurilor
        """
        self.__srv = srv

    def __add_zbor(self):
        """
        Adaugam un nou zbor
        """
        try:
            code = input("Introduceti codul zborului: ")
            duration = int(input("Introduceti durata zborului: "))
            departure = input("Introduceti orasul de plecare: ")
            destination = input("Introduceti orasul de sosire: ")

            zbor = self.__srv.add_zbor(code, duration, departure, destination)
        except ValueError as ve:
            print(ve)

    def __delete_zbor(self):
        """
        Stergem un anumit zbor
        """
        try:
            code = input("Introduceti codul zborului de sters: ")
            self.__srv.delete_zbor(code)
        except ValueError as ve:
            print(ve)

    def __raport(self):
        """
        Creeam raportul zborurilor
        """
        departure_city = input("Introduceti orasul de plecare: ")
        raport = self.__srv.show_zboruri_departure_city(departure_city)

        #afisam raportul
        underlined_string = "   " + "\033[4m" + "Zborurile ordonate alfabetic dupa orasul de sosire" + "\033[0m"
        print("\n")
        print(colored(underlined_string, "cyan"))
        print("\n")
        for elem in raport:
            print(colored("cod:", "blue"), end = " ")
            print(elem[0], end = "  ")
            print(colored("durata:", "green"), end = " ")
            print(elem[1], end = " ")
            print(" minute", end = "  ")
            print(colored("oras de plecare:", "red"), end = " ")
            print(elem[2], end = "  ")
            print(colored("oras de sosire:", "magenta"), end = " ")
            print(elem[3])

    def __modify_zbor(self):
        """
        Modificam zborurile incrementand durata zborurilor
        """
        try:
            departure_city = input("Introduceti orasul de plecare: ")
            duration = int(input("Introduceti durata de adaugat: "))
            self.__srv.increase_duration(departure_city, duration)
        except ValueError as ve:
            print(ve)

    def __show_all(self):
        """
        Returnam toate zborurile
        """
        return self.__srv.get_all()

    def show_ui(self):
        print("\n")
        print("   Bine ati venit la aeroport!   \n")

        exit = False
        while not (exit):
            print("\n")
            print("Lista de zboruri: ", self.__show_all())
            print("\n")
            
            printMeniu()
            optiune = input("Introduceti optiunea: ").strip()
            if optiune == '0':
                print("\nLa revedere!")
                exit = True
            else:
                if optiune == '1':
                    self.__add_zbor()
                elif optiune == '2':
                    self.__delete_zbor()
                elif optiune == '3':
                    self.__raport()
                elif optiune == '4':
                    self.__modify_zbor()
                else:
                    print(colored("Comanda invalida!", "red"), "\n")
                