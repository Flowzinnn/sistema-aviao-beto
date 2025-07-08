import os
from Entities.Flight import Flight
from Entities.Enums import CrewRole
from GeneratorFaker import GeneratorFaker
from BookingSystem import BookingSystem
from MenuBooking import BookingMenu


class AdminMenu:
    def __init__(self):
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
        self.main_menu()

    def main_menu(self):
        while True:
            print("MENU PRINCIPAL")
            print("1 - Menu Administrador")
            print("2 - Sistema de Reservas")
            print("0 - Sair")
            option = input("Digite sua opcao: ")

            if option == "1":
                self.admin_menu()
            elif option == "2":
                booking_menu = BookingMenu(self._flights, self._booking_system)
                booking_menu.start()
            elif option == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opcao invalida!")
                input("Pressione Enter para continuar...")

    def admin_menu(self):
        while True:
            self.clear_screen()
            print("MENU ADMINISTRADOR")
            print("1 - Ver voos disponiveis")
            print("0 - Voltar")
            option = input("Digite sua opcao: ")

            if option == "1":
                self.select_flight()
            elif option == "0":
                break
            else:
                print("Opcao invalida!")
                input("Pressione Enter para continuar...")

    def select_flight(self):
        self.clear_screen()
        print("VOOS DISPONIVEIS")
        for flight in self._flights:
            print(flight)

        selected_id = input("Digite o ID do voo: ")
        selected_flight = None
        for f in self._flights:
            if f.flight_id == selected_id:
                selected_flight = f
                break

        if selected_flight:
            self.flight_menu(selected_flight)
        else:
            print("Voo nao encontrado!")
            input("Pressione Enter para continuar...")

    def flight_menu(self, flight):
        while True:
            self.clear_screen()
            print(f"VOO {flight.flight_id}")
            print("1 - Ver tripulacao")
            print("2 - Ver modelo do aviao")
            print("3 - Ver assento especifico")
            print("0 - Voltar")
            option = input("Digite sua opcao: ")

            if option == "1":
                self.show_crew_menu(flight)
            elif option == "2":
                print(f"Modelo do aviao: {flight.airplane_model}")
                input("Pressione Enter para continuar...")
            elif option == "3":
                number = input("Digite o numero do assento: ")
                seat = flight.get_seat(number)
                if seat:
                    passenger = seat.get_passenger()
                    if passenger:
                        print(f"Assento: {seat.number} | Classe: {seat.seatClass} | Passageiro: {passenger.name}")
                    else:
                        print(f"Assento: {seat.number} | Classe: {seat.seatClass} | Status: LIVRE")
                else:
                    print("Assento nao encontrado.")
                input("Pressione Enter para continuar...")
            elif option == "0":
                break
            else:
                print("Opcao invalida!")
                input("Pressione Enter para continuar...")

    def show_crew_menu(self, flight):
        crew = flight.crew
        crew_list = []
        
        crew_list.append((CrewRole.PILOT.value, crew[CrewRole.PILOT.value]))
        crew_list.append((CrewRole.COPILOT.value, crew[CrewRole.COPILOT.value]))
        for i, attendant in enumerate(crew["Comissários"], start=1):
            crew_list.append((f"Comissario {i}", attendant))
        
        while True:
            self.clear_screen()
            print(f"TRIPULACAO DO VOO {flight.flight_id}")
            for i, (role, member) in enumerate(crew_list, start=1):
                print(f"{i} - {role}: {member.name}")
            print("0 - Voltar")
            option = input("Escolha um tripulante: ")
            
            if option == "0":
                break
            elif option.isdigit():
                index = int(option) - 1
                if 0 <= index < len(crew_list):
                    role, member = crew_list[index]
                    self.show_crew_member_info(role, member)
                else:
                    print("Opcao invalida!")
                    input("Pressione Enter para continuar...")
            else:
                print("Opcao invalida!")
                input("Pressione Enter para continuar...")

    def show_crew_member_info(self, role, member):
        print("INFORMACOES DO TRIPULANTE")
        print(f"Nome: {member.name}")
        print(f"Idade: {member.age}")
        print(f"Funcao: {member.role}")
        print(f"Tipo: {member.type()}")
        input("Pressione Enter para continuar...")
