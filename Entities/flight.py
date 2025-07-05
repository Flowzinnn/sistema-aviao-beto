import random
from Entities.airplane import Airplane, AirplaneModel
from Entities.seat import Seat
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
        self._seats = self._generate_seats()
        self._crew = self._generate_crew()
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

    def _generate_seats(self):
        return [Seat(str(i + 1), "Econômica") for i in range(250)]

    def _generate_crew(self):
        """
        Gera a tripulação do voo: 1 piloto, 1 copiloto e 2 comissários.
        """
        return {
            "Piloto": generate_pilot(),
            "Copiloto": generate_copilot(),
            "Comissários": [generate_attendant(), generate_attendant()]
        }

    def _fill_passengers(self):
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
