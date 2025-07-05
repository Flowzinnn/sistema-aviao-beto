from Entities.defaultPeople import DefaultPeople

class Passenger(DefaultPeople):
    def __init__(self, name: str, CPF: int, age: int):
        super().__init__(name, CPF, age)
        self._flyHistory = []

    @property
    def flyHistory(self):
        return self._flyHistory

    @flyHistory.setter
    def flyHistory(self, value):
        self._flyHistory = value

    def tipo(self) -> str:
        return "Passenger"