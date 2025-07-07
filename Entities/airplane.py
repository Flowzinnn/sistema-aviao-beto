from enum import Enum
from Entities.Enums import AirplaneModel

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
