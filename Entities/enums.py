from enum import Enum

class SeatClass(Enum):
    """
    Enum para as classes de assento disponíveis no avião.
    """
    ECONOMIC = "Econômica"
    EXECUTIVE = "Executiva"
    FIRST_CLASS = "Primeira Classe"

class AirplaneModel(Enum):
    """
    Enum para os modelos de avião disponíveis.
    """
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

class CrewRole(Enum):
    """
    Enum para os cargos da tripulação.
    """
    PILOT = "Piloto"
    COPILOT = "Copiloto"
    FLIGHT_ATTENDANT = "Comissário"
