from faker import Faker
import random
from Entities.Passenger import Passenger
from Entities.CrewMember import Pilot, Copilot, FlightAttendant

class GeneratorFaker:
    def __init__(self):
        """Inicializa o gerador de dados com Faker e configurações brasileiras."""
        self.faker = Faker("pt_BR")
        self.existing_ids = set()

    def generate_passenger(self) -> Passenger:
        """Gera um passageiro com nome, CPF e idade aleatória."""
        name = self.faker.name()
        cpf = self.faker.cpf()
        age = random.randint(18, 80)
        return Passenger(name, cpf, age)

    def generate_pilot(self) -> Pilot:
        """Gera um piloto com nome, CPF e idade aleatória."""
        name = self.faker.name_male()
        cpf = self.faker.cpf()
        age = random.randint(35, 65)
        return Pilot(name, cpf, age)

    def generate_copilot(self) -> Copilot:
        """Gera um copiloto com nome, CPF e idade aleatória."""
        name = self.faker.name_male()
        cpf = self.faker.cpf()
        age = random.randint(30, 60)
        return Copilot(name, cpf, age)

    def generate_attendant(self) -> FlightAttendant:
        """Gera um comissário de bordo com nome, CPF e idade aleatória."""
        name = self.faker.name_female()
        cpf = self.faker.cpf()
        age = random.randint(22, 55)
        return FlightAttendant(name, cpf, age)

    def generate_city_pair(self):
        """Retorna uma tupla (origem, destino) com cidades brasileiras diferentes."""
        origin = self.faker.city()
        destination = self.faker.city()
        while destination == origin:
            destination = self.faker.city()
        return origin, destination

    def generate_flight_id(self):
        """
        Gera um ID de voo único aleatório de 4 dígitos.
        """
        while True:
            flight_id = str(random.randint(1000, 9999))
            if flight_id not in self.existing_ids:
                self.existing_ids.add(flight_id)
                return flight_id
