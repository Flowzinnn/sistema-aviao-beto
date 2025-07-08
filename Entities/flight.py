import random
from Entities.Airplane import Airplane
from Entities.Seat import Seat
from Entities.Enums import AirplaneModel, SeatClass
from GeneratorFaker import GeneratorFaker


class Flight:
    def __init__(self, flight_id: str, origin: str, destination: str, faker: GeneratorFaker):
        
        """Inicializa um voo com ID, origem, destino, avião, tripulação e passageiros."""

        self._flight_id = flight_id
        self._origin = origin
        self._destination = destination
        self._faker = faker
        self._airplane = Airplane(random.choice(list(AirplaneModel)), 250)
        self._seats = self.generateSeats()
        self._crew = self.generateCrew()
        self.fillPassengers()

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
            "Piloto": self._faker.generate_pilot(),
            "Copiloto": self._faker.generate_copilot(),
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
        return f"{self.flight_id} - {self.origin} → {self.destination} ({self.airplane_model})"


    def get_seat(self, number: str):
        for seat in self.seats:
            if seat.number == number:
                return seat
        return None
