from faker import Faker
import random
from Entities.passenger import Passenger
from Entities.crewMember import Pilot, Copilot, FlightAttendant

faker = Faker("pt_BR")


def generate_passenger() -> Passenger:
    """Gera um passageiro com nome, CPF e idade aleatória."""
    name = faker.name()
    cpf = faker.cpf()
    age = random.randint(18, 80)
    return Passenger(name, cpf, age)


def generate_pilot() -> Pilot:
    """Gera um piloto com nome, CPF e idade aleatória."""
    name = faker.name_male()
    cpf = faker.cpf()
    age = random.randint(35, 65)
    return Pilot(name, cpf, age)


def generate_copilot() -> Copilot:
    """Gera um copiloto com nome, CPF e idade aleatória."""
    name = faker.name_male()
    cpf = faker.cpf()
    age = random.randint(30, 60)
    return Copilot(name, cpf, age)


def generate_attendant() -> FlightAttendant:
    """Gera um comissário de bordo com nome, CPF e idade aleatória."""
    name = faker.name_female()
    cpf = faker.cpf()
    age = random.randint(22, 55)
    return FlightAttendant(name, cpf, age)
