import os
from typing import List
from BookingSystem import BookingSystem
from Entities.Flight import Flight
from Entities.Passenger import Passenger
from GeneratorFaker import GeneratorFaker


class BookingMenu:
    def __init__(self, flights: List[Flight], booking_system: BookingSystem):
        self._flights = flights
        self._booking_system = booking_system
        self._faker = GeneratorFaker()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        self.clear_screen()
        self.main_booking_menu()

    def main_booking_menu(self):
        while True:
            print("SISTEMA DE RESERVAS")
            print("1 - Fazer nova reserva")
            print("2 - Consultar reserva")
            print("3 - Cancelar reserva")
            print("4 - Ver voos disponiveis")
            print("5 - Estatisticas do sistema")
            print("0 - Voltar ao menu principal")
            
            option = input("Escolha uma opcao: ")
            
            if option == "1":
                self.make_reservation()
            elif option == "2":
                self.check_reservation()
            elif option == "3":
                self.cancel_reservation()
            elif option == "4":
                self.show_available_flights()
            elif option == "5":
                self.show_statistics()
            elif option == "0":
                break
            else:
                print("[ERRO] Opcao invalida!")
                input("Pressione Enter para continuar...")

    def make_reservation(self):
        self.clear_screen()
        print("NOVA RESERVA")
        
        print("\nVoos Disponiveis:")
        for flight in self._flights:
            available_seats = self._booking_system.get_available_seats(flight)
            print(f"ID: {flight.flight_id} | {flight.get_info()} | {len(available_seats)} assentos livres")
        
        flight_id = input("\nDigite o ID do voo: ")
        selected_flight = None
        
        for flight in self._flights:
            if flight.flight_id == flight_id:
                selected_flight = flight
                break
        
        if not selected_flight:
            print("[ERRO] Voo nao encontrado!")
            input("Pressione Enter para continuar...")
            return
        
        self.show_available_seats(selected_flight)
        
        print("\nDados do Passageiro:")
        name = input("Nome: ")
        cpf = input("CPF: ")
        try:
            age = int(input("Idade: "))
        except ValueError:
            print("[ERRO] Idade invalida!")
            input("Pressione Enter para continuar...")
            return
        
        passenger = Passenger(name, cpf, age)
        
        seat_number = input("\nNumero do assento desejado: ")
        
        try:
            booking_code = self._booking_system.book_seat(selected_flight, seat_number, passenger)
            print("\nRESERVA REALIZADA COM SUCESSO!")
            print(f"Codigo de reserva: {booking_code}")
            print(f"Voo: {selected_flight.flight_id}")
            print(f"Assento: {seat_number}")
            print(f"Passageiro: {name}")
            
        except ValueError as e:
            print(f"[ERRO] {e}")
            input("Pressione Enter para continuar...")
        
        input("\nPressione Enter para continuar...")

    def show_available_seats(self, flight: Flight):
        print(f"\nAssentos Disponiveis - Voo {flight.flight_id}:")
        
        classes = {
            "Primeira Classe": [],
            "Executiva": [],
            "Economica": []
        }
        
        available_seats = self._booking_system.get_available_seats(flight)
        
        for seat in available_seats:
            if seat.seatClass == "Primeira Classe":
                classes["Primeira Classe"].append(seat.number)
            elif seat.seatClass == "Executiva":
                classes["Executiva"].append(seat.number)
            else:
                classes["Economica"].append(seat.number)
        
        for seat_class, seats in classes.items():
            if seats:
                print(f"\n{seat_class}: {len(seats)} disponiveis")
                seats_to_show = seats[:10]
                print(f"Assentos: {', '.join(seats_to_show)}")
                if len(seats) > 10:
                    print(f"... e mais {len(seats) - 10} assentos")

    def check_reservation(self):
        self.clear_screen()
        print("CONSULTAR RESERVA")
        
        booking_code = input("Digite o codigo da reserva: ")
        
        reservation = self._booking_system.get_booking(booking_code)
        
        if reservation:
            print("\nRESERVA ENCONTRADA")
            print(f"Codigo: {booking_code}")
            print(f"Voo: {reservation.flight.flight_id}")
            print(f"Origem: {reservation.flight.origin}")
            print(f"Destino: {reservation.flight.destination}")
            print(f"Assento: {reservation.seat.number}")
            print(f"Classe: {reservation.seat.seatClass}")
            print(f"Passageiro: {reservation.passenger.name}")
            print(f"Data da reserva: {reservation.booking_date.strftime('%d/%m/%Y %H:%M')}")
            print(f"Status: {reservation.status}")
        else:
            print("[ERRO] Reserva nao encontrada!")
        
        input("\nPressione Enter para continuar...")

    def cancel_reservation(self):
        self.clear_screen()
        print("CANCELAR RESERVA")
        
        booking_code = input("Digite o codigo da reserva: ")
        
        if self._booking_system.cancel_booking(booking_code):
            print("\nRESERVA CANCELADA COM SUCESSO!")
        else:
            print("[ERRO] Reserva nao encontrada!")
        
        input("\nPressione Enter para continuar...")

    def show_available_flights(self):
        self.clear_screen()
        print("VOOS DISPONIVEIS")
        
        for flight in self._flights:
            available_seats = self._booking_system.get_available_seats(flight)
            
            if available_seats:
                print(f"\n{flight.get_info()}")
                print(f"Assentos disponiveis: {len(available_seats)}")
                
                classes_count = {}
                for seat in available_seats:
                    classes_count[seat.seatClass] = classes_count.get(seat.seatClass, 0) + 1
                
                for seat_class, count in classes_count.items():
                    print(f"{seat_class}: {count} assentos")
        
        input("\nPressione Enter para continuar...")

    def show_statistics(self):
        self.clear_screen()
        print("ESTATISTICAS DO SISTEMA")
        
        stats = self._booking_system.get_booking_statistics()
        
        print(f"\nResumo Geral:")
        print(f"Reservas totais: {stats['total_bookings']}")
        print(f"Reservas ativas: {stats['active_bookings']}")
        print(f"Reservas canceladas: {stats['cancelled_bookings']}")
        
        print(f"\nEstatisticas do Voo:")
        for flight in self._flights:
            total_seats = len(flight.seats)
            available_seats = len(self._booking_system.get_available_seats(flight))
            occupied_seats = total_seats - available_seats
            occupancy_rate = (occupied_seats / total_seats) * 100
            
            print(f"{flight.flight_id}: {occupied_seats}/{total_seats} ({occupancy_rate:.1f}%)")
        
        input("\nPressione Enter para continuar...")