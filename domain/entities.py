from termcolor import colored

class Zbor:
    def __init__(self, code, duration, departure, destination):
        """
        Functia constructor a clasei Zbor
        :param code: cod-ul zborului
        :param duration: durata zborului
        :param departure: orasul din decoleaza
        :param destination: orasul in care aterizeaza
        """
        self.__code = code
        self.__duration = duration
        self.__departure = departure
        self.__destination = destination

    """
    Getters si setteri pt clasa Zbor
    """

    def getCode(self):
        return self.__code
    def getDuration(self):
        return self.__duration
    def getDeparture(self):
        return self.__departure
    def getDestination(self):
        return self.__destination
    
    def setDuration(self, value):
        self.__duration = value
    def setDeparture(self, value):
        self.__departure = value
    def setDestination(self, value):
        self.__destination = value

    def __eq__(self, other):
        return self.__code == other.__code and self.__duration == other.__duration and self.__departure == other.__departure and self.__departure == other.__destination
    def __str__(self):
        return colored("code: ", "blue") + str(self.__code) + "; duration: " + str(self.__duration) + "; departure: " + str(self.__departure) + "; destination: " + str(self.__destination) + colored("; ", "red")
    def __repr__(self):
        return str(self)
    
#teste

def test_create_zbor():
    zbor = Zbor("0544b3", 254, "Cluj-Napoca", "Bucuresti")
    assert zbor.getCode() == "0544b3"
    assert zbor.getDuration() == 254
    assert zbor.getDeparture() == "Cluj-Napoca"
    assert zbor.getDestination() == "Bucuresti"

test_create_zbor()