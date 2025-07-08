import random
from typing import Optional
from Entities.Airplane import Airplane
from Entities.Seat import Seat
from Entities.Enums import AirplaneModel, SeatClass, CrewRole
from GeneratorFaker import GeneratorFaker


class Flight:
    
    """
    Inicializa um voo com ID, origem, destino, avião, tripulação e passageiros.
    """

    def __init__(self, flight_id: str, origin: str, destination: str, faker: GeneratorFaker):
        self._flight_id = flight_id
        self._origin = origin
        self._destination = destination
        self._faker = faker
        self._airplane = Airplane(random.choice(list(AirplaneModel)))
        self._seats = self.generateSeats()
        self._seat_map = {seat.number: seat for seat in self._seats}
        self._crew = self.generateCrew()
        self.fillPassengers()
        
        
    def __str__(self):
        return f"FlightID:({self._flight_id}) <> Voo de {self._origin} com destino à {self._destination} <> Avião: {self.airplane_model}"

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
    
    @property
    def airplane_model(self):
        return self.airplane.model.value

    def generateSeats(self):
        """
        Gera os assentos do voo baseado na capacidade real do avião.
        """
        seats = []
        distribution = self._airplane.get_seat_distribution()
        seat_number = 1
        
        # Primeira Classe
        for i in range(distribution['first_class']):
            seats.append(Seat(str(seat_number), SeatClass.FIRST_CLASS.value))
            seat_number += 1
        
        # Executiva
        for i in range(distribution['executive']):
            seats.append(Seat(str(seat_number), SeatClass.EXECUTIVE.value))
            seat_number += 1
        
        # Econômica
        for i in range(distribution['economic']):
            seats.append(Seat(str(seat_number), SeatClass.ECONOMIC.value))
            seat_number += 1
        
        return seats
        
    def generateCrew(self):
        """
        Gera a tripulação do voo: 1 piloto, 1 copiloto e 2 comissários.
        """
        return {
            CrewRole.PILOT.value: self._faker.generate_pilot(),
            CrewRole.COPILOT.value: self._faker.generate_copilot(),
            "Comissários": [
                self._faker.generate_attendant(),
                self._faker.generate_attendant()
            ]
        }

    def fillPassengers(self):
        """
        Preenche automaticamente alguns assentos com passageiros.
        Agora usa o BookingSystem para manter a consistência.
        """
        # Importação local para evitar dependência circular
        from BookingSystem import BookingSystem
        
        booking_system = BookingSystem()
        
        # Preenche apenas 80% dos assentos para deixar alguns livres
        seats_to_fill = int(len(self._seats) * 0.8)
        
        for i in range(seats_to_fill):
            seat = self._seats[i]
            if not seat.is_reserved():
                passenger = self._faker.generate_passenger()
                try:
                    booking_system.book_seat(self, seat.number, passenger)
                except ValueError:
                    # Assento já reservado, pular
                    continue

    def get_info(self):
        return f" {self.origin} → {self.destination} ({self.airplane_model})"


    def get_seat(self, number: str) -> Optional[Seat]:
        """ Args: Number: Número do assento; Tipo string"""
        return self._seat_map.get(number)
