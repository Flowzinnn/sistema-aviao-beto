from enum import Enum

class AirplaneModel(Enum):
    BOEING_737 = "Boeing 737"
    BOEING_747 = "Boeing 747"
    BOEING_777 = "Boeing 777"
    BOEING_787 = "Boeing 787 Dreamliner"
    AIRBUS_A320 = "Airbus A320"
    AIRBUS_A330 = "Airbus A330"
    AIRBUS_A350 = "Airbus A350"
    AIRBUS_A380 = "Airbus A380"
    EMBRAER_E190 = "Embraer E190"
    EMBRAER_E195 = "Embraer E195"

class Airplane:
    def __init__(self, model: AirplaneModel, capacity: int):
        self._model = model
        self._capacity = capacity

    @property
    def model(self):
        """ Retorna o modelo do avião. """
        return self._model

    @property
    def capacity(self):
        """ Retorna a capacidade do avião. """
        return self._capacity
