import os
from Entities.Flight import Flight
from GeneratorFaker import GeneratorFaker


class AdminMenu:
    def __init__(self):
        """
        Inicializa o menu do administrador e cria os voos com dados gerados pelo Faker.
        """
        self._faker = GeneratorFaker()
        self._flights = []
        self._generate_flights()

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _generate_flights(self):
        for _ in range(10):
            origin, destination = self._faker.generate_city_pair()
            flight_id = self._faker.generate_flight_id()
            self._flights.append(Flight(flight_id, origin, destination, self._faker))

    def start(self):
        self._clear_screen()
        self._main_menu()

    def _main_menu(self):
        while True:
            print("=== Menu Administrador ===")
            print("1 - Ver voos disponíveis")
            print("0 - Sair")
            option = input("Escolha uma opção: ")

            if option == "1":
                self._clear_screen()
                self._select_flight()
            elif option == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

    def _select_flight(self):
        print("=== Voos Disponíveis ===")
        for flight in self._flights:
            print(flight.get_info())

        selected_id = input("\nDigite o ID do voo que deseja visualizar: ")
        selected_flight = None
        for f in self._flights:
            if f.flight_id == selected_id:
                selected_flight = f
                break

        if selected_flight:
            self._flight_menu(selected_flight)
        else:
            print("Voo não encontrado.")

    def _flight_menu(self, flight):
        while True:
            print(f"\n=== Voo {flight.flight_id} ===")
            print("1 - Ver tripulação")
            print("2 - Ver modelo do avião")
            print("3 - Ver assento específico")
            print("0 - Voltar")

            option = input("Escolha uma opção: ")

            if option == "1":
                crew = flight.get_crew()
                print(f"\nPiloto: {crew['Piloto'].name}")
                print(f"Copiloto: {crew['Copiloto'].name}")
                for i, attendant in enumerate(crew["Comissários"], start=1):
                    print(f"Comissário {i}: {attendant.name}")
            elif option == "2":
                print(f"\nModelo do avião: {flight.get_airplane_model()}")
            elif option == "3":
                number = input("Digite o número do assento: ")
                seat = flight.get_seat(number)
                if seat:
                    passenger = seat.get_passenger()
                    print(f"FlightID: {flight.flight_id} | Assento: {seat.number} | Classe: {seat.seatClass} | Passageiro: {passenger.name}")
                else:
                    print("Assento não encontrado.")
            elif option == "0":
                self._clear_screen()
                break
            else:
                print("Opção inválida.")
