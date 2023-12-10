from domain.entities import Zbor
from termcolor import colored

class ZborValidator:
    def valideaza_zborul(self, zbor):
        erori = []
        if len(zbor.getCode()) < 3:
            erori.append(colored("Codul zborului nu poate avea mai putin de 3 caractere!", "red"))
        if zbor.getDuration() < 20:
            erori.append(colored("Durata zborului nu poate fi mai mica de 20 de minute!", "red"))
        if len(zbor.getDeparture()) < 3:
            erori.append(colored("Departure-ul zborului nu poate avea mai putin de 3 caractere!", "red"))
        if len(zbor.getDestination()) < 3:
            erori.append(colored("Destinatia zborului nu poate avea mai putin de 3 caractere!", "red"))
        if len(erori) > 0:
            raise ValueError(erori)
        
def test_ZborValidator():
    validator = ZborValidator()

    zbor = Zbor("0544b3", 254, "Cluj-Napoca", "Bucuresti")
    validator.valideaza_zborul(zbor)

    zbor = Zbor("", 254, "Cluj-Napoca", "Bucuresti")
    try:
        validator.valideaza_zborul(zbor)
        assert False
    except ValueError:
        assert True

    zbor = Zbor("0544b3", 12, "Cluj-Napoca", "Bucuresti")
    try:
        validator.valideaza_zborul(zbor)
        assert False
    except ValueError:
        assert True

    zbor = Zbor("0544b3", 254, "Cluj-Napoca", "B")
    try:
        validator.valideaza_zborul(zbor)
        assert False
    except ValueError:
        assert True

    zbor = Zbor("0544b3", 254, "C", "Bucuresti")
    try:
        validator.valideaza_zborul(zbor)
        assert False
    except ValueError:
        assert True
        
test_ZborValidator()