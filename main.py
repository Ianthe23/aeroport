from domain.entities import Zbor
from domain.validators import ZborValidator
from repository.repo import OperatiiZboruriFile
from service.service import ZborService
from ui.console import Console

Zborul = ZborService(OperatiiZboruriFile("zboruri.txt"), ZborValidator())

ui = Console(Zborul)

ui.show_ui()