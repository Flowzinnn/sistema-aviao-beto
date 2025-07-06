import random
from Entities.airplane import Airplane
from Entities.seat import Seat
from Entities.enums import AirplaneModel, SeatClass
from generatorFaker import (
    generate_passenger,
    generate_pilot,
    generate_copilot,
    generate_attendant
)

class Flight:
    def __init__(self, flight_id: str, origin: str, destination: str):
        self._flight_id = flight_id
        self._origin = origin
        self._destination = destination
        self._airplane = Airplane(random.choice(list(AirplaneModel)), 250)
        self._seats = self._generateSeats()
        self._crew = self._generateCrew()
        self._fill_passengers()

    @property
    def flight_id(self):
        return self._flight_id

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def airplane(self):
        return self._airplane

    @property
    def seats(self):
        return self._seats

    @property
    def crew(self):
        return self._crew

    def generateSeats(self):
        """
        Gera os assentos do voo, 25 Primeira Classe, 75 Executiva e 150 Econômica.
        """
        seats = []
        
        # Primeira Classe: assentos 1-25
        seats.extend([Seat(str(i), SeatClass.FIRST_CLASS.value) for i in range(1, 26)])
        
        # Executiva: assentos 26-100  
        seats.extend([Seat(str(i), SeatClass.EXECUTIVE.value) for i in range(26, 101)])
        
        # Econômica: assentos 101-250
        seats.extend([Seat(str(i), SeatClass.ECONOMIC.value) for i in range(101, 251)])
        
        return seats
        
    def generateCrew(self):
        """
        Gera a tripulação do voo: 1 piloto, 1 copiloto e 2 comissários.
        """
        return {
            "Piloto": generate_pilot(),
            "Copiloto": generate_copilot(),
            "Comissários": [generate_attendant(), generate_attendant()]
        }

    def fill_passengers(self):
        for seat in self._seats:
            seat.reserve(generate_passenger())

    def get_info(self):
        return f"{self.flight_id} - {self.origin} → {self.destination} ({self.airplane.model.value})"

    def get_airplane_model(self):
        return self.airplane.model.value

    def get_crew(self):
        return self.crew

    def get_seat(self, number: str):
        for seat in self.seats:
            if seat.number == number:
                return seat
        return None
