import os
from Entities.Flight import Flight
from GeneratorFaker import GeneratorFaker
from BookingSystem import BookingSystem
from MenuBooking import BookingMenu


class AdminMenu:
    def __init__(self):
        """
        Inicializa o menu do administrador e cria os voos com dados gerados pelo Faker.
        """
        self._faker = GeneratorFaker()
        self._flights = []
        self._booking_system = BookingSystem()
        self.generate_flights()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_flights(self):
        for _ in range(10):
            origin, destination = self._faker.generate_city_pair()
            flight_id = self._faker.generate_flight_id()
            self._flights.append(Flight(flight_id, origin, destination, self._faker))

    def start(self):
        self.clear_screen()
        self._main_menu()

    def _main_menu(self):
        while True:
            print("=== Menu Principal ===")
            print("1 - Menu Administrador")
            print("2 - Sistema de Reservas")
            print("0 - Sair")
            option = input("Escolha uma opção: ")

            if option == "1":
                self._admin_menu()
            elif option == "2":
                booking_menu = BookingMenu(self._flights, self._booking_system)
                booking_menu.start()
            elif option == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

    def _admin_menu(self):
        while True:
            print("\n=== Menu Administrador ===")
            print("1 - Ver voos disponíveis")
            print("0 - Voltar")
            option = input("Escolha uma opção: ")

            if option == "1":
                self.clear_screen()
                self._select_flight()
            elif option == "0":
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
                self._show_crew_menu(flight)
            elif option == "2":
                print(f"\nModelo do avião: {flight.airplane_model}")
            elif option == "3":
                number = input("Digite o número do assento: ")
                seat = flight.get_seat(number)
                if seat:
                    passenger = seat.get_passenger()
                    if passenger:
                        print(f"FlightID: {flight.flight_id} | Assento: {seat.number} | Classe: {seat.seatClass} | Passageiro: {passenger.name}")
                    else:
                        print(f"FlightID: {flight.flight_id} | Assento: {seat.number} | Classe: {seat.seatClass} | Status: LIVRE")
                else:
                    print("Assento não encontrado.")
            elif option == "0":
                self.clear_screen()
                break
            else:
                print("Opção inválida!")

    def _show_crew_menu(self, flight):
        """
        Mostra o menu da tripulação com opções para ver informações públicas.
        """
        crew = flight.crew
        crew_list = []
        
        # Criar lista ordenada da tripulação
        crew_list.append(("Piloto", crew['Piloto']))
        crew_list.append(("Copiloto", crew['Copiloto']))
        for i, attendant in enumerate(crew["Comissários"], start=1):
            crew_list.append((f"Comissário {i}", attendant))
        
        while True:
            print(f"\n=== Tripulação do Voo {flight.flight_id} ===")
            for i, (role, member) in enumerate(crew_list, start=1):
                print(f"{i} - {role}: {member.name}")
            print("0 - Voltar")
            
            option = input("\nEscolha um tripulante para ver informações públicas: ")
            
            if option == "0":
                break
            elif option.isdigit():
                index = int(option) - 1
                if 0 <= index < len(crew_list):
                    role, member = crew_list[index]
                    self._show_crew_member_info(role, member)
                else:
                    print("Opção inválida!")
            else:
                print("Opção inválida!")

    def _show_crew_member_info(self, role, member):
        """
        Mostra as informações públicas de um tripulante.
        """
        print(f"\n=== Informações Públicas - {role} ===")
        print(f"Nome: {member.name}")
        print(f"Idade: {member.age}")
        print(f"Função: {member.role}")
        print(f"Tipo: {member.type()}")
        input("\nPressione Enter para continuar...")
