from Entities.defaultPeople import DefaultPeople

class CrewMember(DefaultPeople):
    def __init__(self, name: str, cpf: str, age: int, role: str):
        super().__init__(name, cpf, age)
        self._role = role

    @property
    def role(self):
        """ Retorna a função do tripulante (Pilot, Copilot, Flight Attendant). """
        return self._role

    def type(self) -> str:
        """ Retorna o tipo de pessoa (tripulante). """
        return "CrewMember"


class Pilot(CrewMember):
    def __init__(self, name: str, cpf: str, age: int) -> None:
        """Cria um Piloto."""
        super().__init__(name, cpf, age, "Pilot")


class Copilot(CrewMember):
    def __init__(self, name: str, cpf: str, age: int) -> None:
        """Cria um Copiloto."""
        super().__init__(name, cpf, age, "Copilot")


class FlightAttendant(CrewMember):
    def __init__(self, name: str, cpf: str, age: int) -> None:
        """Cria um Comissário de bordo."""
        super().__init__(name, cpf, age, "Flight Attendant")
