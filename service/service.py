from domain.entities import Zbor
from domain.validators import ZborValidator
from repository.repo import OperatiiZboruriFile
from termcolor import colored

class ZborService:
    def __init__(self, repo, validator):
        """
        Metode constructor a serverului GRASP
        :param repo: repository-ul
        """
        self.__repo = repo
        self.__validator = validator

    def add_zbor(self, code, duration, departure, destination):
        """
        Incearca sa introduca zborul in memorie
        :param code: cod-ul zborului de adaugat
        :param duration: durata zborului de adaugat
        :param departure: orasul de plecare al avionului
        :param destination: orasul de aterizare al avionului
        """
        zbor = Zbor(code, duration, departure, destination)
        self.__validator.valideaza_zborul(zbor)
        self.__repo.adauga_zbor(zbor)
        return zbor
    
    def delete_zbor(self, code):
        """
        Functia sterge zborul identificat prin codul dat
        """
        self.__repo.sterge_zbor(code)

    def create_raport(self, departure_city):
        """
        Functia creeaza un raport al zborurilor dupa orasul de plecare
        :param departure_city: orasul de plecare
        """
        lista_zboruri = self.__repo.returneaza_zboruri()
        raport = []
        for zbor in lista_zboruri:
            if zbor.getDeparture() == departure_city:
                raport.append([zbor.getCode(), zbor.getDuration(), zbor.getDeparture(), zbor.getDestination()])

        return raport
    
    def show_zboruri_departure_city(self, departure_city):
        """
        Functia imi ordoneaza raportul in functie de orasul destinatie
        :param departure_city: orasul de plecare
        """
        raport = self.create_raport(departure_city)

        raport_sortat = sorted(raport, key = lambda x: x[3])
        return raport_sortat

    def increase_duration(self, departure_city, duration):
        """
        Functia imi modifica zborurile cu departure_city si noul duration
        :param departure_city: orasul de plecare
        :param duration: durata de adaugat
        """
        if duration < 10 or duration > 60:
            raise ValueError(colored("Durata nu respecta limitele!", "red"))
        else:
            self.__repo.modifica_zbor(departure_city, duration)
        
    def get_all(self):
        """
        Returnam zborurile din repo
        """
        return self.__repo.returneaza_zboruri()
        
    


