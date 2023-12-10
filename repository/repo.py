from domain.entities import Zbor
import os
from termcolor import colored

class OperatiiZboruriFile():
    def __init__(self, filename):
        """
        Metoda constructor a clasei OperatiiZboruriFile
        :param filename: fisierul din care citim
        """
        self.__zboruri = []
        file = os.path.abspath(filename)
        self.__filename = file
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citim datele din fisier
        """
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line == "\n":
                    break
                code, duration, departure, destination = [elem.strip() for elem in line.split(", ")]
                zbor = Zbor(code, duration, departure, destination)
                self.__zboruri.append(zbor)
    
    def __save_to_file(self):
        """
        Salvam in fisier 
        """
        with open(self.__filename, "w") as f:
            toate_zborurile = self.returneaza_zboruri()
            for zbor in toate_zborurile:
                zbor_de_salvat = str(zbor.getCode()) + ", " + str(zbor.getDuration()) + ", " + str(zbor.getDeparture()) + ", " + str(zbor.getDestination()) + "\n"
                f.write(zbor_de_salvat)

    def adauga_zbor(self, zbor_nou):
        """
        Adaugam un zbor
        :param zbor_nou: Un zbor nou
        """
        for zbor in self.__zboruri:
            if zbor.getCode() == zbor_nou.getCode():
                raise ValueError(colored("Codul exista deja!", "red"))
        self.__zboruri.append(zbor_nou)
        self.__save_to_file()

    def sterge_zbor(self, code):
        """
        Stergem un zbor
        :param code: Codul zborului pe care-l stergem
        """
        ok = 1
        for index in range(len(self.__zboruri)):
            if self.__zboruri[index].getCode() == code:
                self.__zboruri.pop(index)
                ok = 0
                break
        if ok:
            raise ValueError(colored("Nu exista zborul cu acest cod!", "red"))
        self.__save_to_file()

    def modifica_zbor(self, departure_city, duration):
        """
        Functia modifica zborurile identificate prin departure_city cu duration
        :param departure_city: orasul de plecare
        :param duration: durata de adaugat
        """
        ok = 1
        for index in range(len(self.__zboruri)):
            if self.__zboruri[index].getDeparture() == departure_city:
                ok = 0
                self.__zboruri[index].setDuration(int(self.__zboruri[index].getDuration()) + duration)
        if ok:
            raise ValueError(colored("Nu exista astfel de zboruri de modificat!", "red"))
        self.__save_to_file()
        
    
    def returneaza_zboruri(self):
        return self.__zboruri
        
    def __eq__(self, other):
        return self.__zboruri == other.__zboruri
    
def test_adauga_zbor():
    repo = OperatiiZboruriFile("test_repo.txt")
    assert repo.returneaza_zboruri() == []

    zbor = Zbor("0544b3", 254, "Cluj-Napoca", "Bucuresti")
    repo.adauga_zbor(zbor)
    assert len(repo.returneaza_zboruri()) == 1

def test_sterge_zbor():
    repo = OperatiiZboruriFile("test_repo.txt")
    assert len(repo.returneaza_zboruri()) == 1

    zbor = Zbor("0544b2", 254, "Cluj-Napoca", "Bucuresti")
    repo.adauga_zbor(zbor)
    assert len(repo.returneaza_zboruri()) == 2

    repo.sterge_zbor("0544b3")
    assert len(repo.returneaza_zboruri()) == 1

def test_modifica_zbor():
    repo = OperatiiZboruriFile("test_repo.txt")
    assert len(repo.returneaza_zboruri()) == 1

    zbor = Zbor("0544b3", 254, "Cluj-Napoca", "Bucuresti")
    repo.adauga_zbor(zbor)
    assert len(repo.returneaza_zboruri()) == 2

    repo.modifica_zbor("Cluj-Napoca", 32)
    lista = repo.returneaza_zboruri()
    assert lista[0].getDuration() == 286
    assert lista[1].getDuration() == 286

test_adauga_zbor()
test_sterge_zbor()
test_modifica_zbor()

