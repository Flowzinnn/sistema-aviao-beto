import os
from typing import List
from BookingSystem import BookingSystem
from Entities.Flight import Flight
from Entities.Passenger import Passenger
from GeneratorFaker import GeneratorFaker


class BookingMenu:
    """
    Menu interativo para sistema de reservas.
    Permite aos usuários fazer reservas, cancelar e consultar.
    """
    
    def __init__(self, flights: List[Flight], booking_system: BookingSystem):
        self._flights = flights
        self._booking_system = booking_system
        self._faker = GeneratorFaker()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        """Inicia o menu de reservas."""
        self.clear_screen()
        self.main_booking_menu()

    def main_booking_menu(self):
        """Menu principal do sistema de reservas."""
        while True:
            print("\n" + "="*50)
            print("🎫 SISTEMA DE RESERVAS ✈️")
            print("="*50)
            print("1 - Fazer nova reserva")
            print("2 - Consultar reserva")
            print("3 - Cancelar reserva")
            print("4 - Ver voos disponíveis")
            print("5 - Estatísticas do sistema")
            print("0 - Voltar ao menu principal")
            print("="*50)
            
            option = input("Escolha uma opção: ")
            
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
                print("❌ Opção inválida!")
                input("Pressione Enter para continuar...")

    def make_reservation(self):
        """Processo de fazer uma nova reserva."""
        self.clear_screen()
        print("🆕 NOVA RESERVA")
        print("="*30)
        
        # Mostrar voos disponíveis
        print("\n📋 Voos Disponíveis:")
        for flight in self._flights:
            available_seats = self._booking_system.get_available_seats(flight)
            print(f"ID: {flight.flight_id} - {flight.get_info()} - {len(available_seats)} assentos livres")
        
        # Selecionar voo por ID
        flight_id = input("\nDigite o ID do voo: ")
        selected_flight = None
        
        for flight in self._flights:
            if flight.flight_id == flight_id:
                selected_flight = flight
                break
        
        if not selected_flight:
            print("❌ Voo não encontrado!")
            input("Pressione Enter para continuar...")
            return
        
        # Mostrar assentos disponíveis
        self.show_available_seats(selected_flight)
        
        # Dados do passageiro
        print("\n👤 Dados do Passageiro:")
        name = input("Nome: ")
        cpf = input("CPF: ")
        try:
            age = int(input("Idade: "))
        except ValueError:
            print("❌ Idade inválida!")
            return
        
        passenger = Passenger(name, cpf, age)
        
        # Selecionar assento
        seat_number = input("Número do assento desejado: ")
        
        # Fazer reserva
        try:
            booking_code = self._booking_system.book_seat(selected_flight, seat_number, passenger)
            print(f"\n✅ Reserva realizada com sucesso!")
            print(f"🎫 Código de reserva: {booking_code}")
            print(f"✈️  Voo: {selected_flight.flight_id}")
            print(f"💺 Assento: {seat_number}")
            print(f"👤 Passageiro: {name}")
            
        except ValueError as e:
            print(f"❌ Erro na reserva: {e}")
        
        input("\nPressione Enter para continuar...")

    def show_available_seats(self, flight: Flight):
        """Mostra assentos disponíveis por classe."""
        print(f"\n💺 Assentos Disponíveis - Voo {flight.flight_id}:")
        
        # Agrupar por classe
        classes = {
            "Primeira Classe": [],
            "Executiva": [],
            "Econômica": []
        }
        
        available_seats = self._booking_system.get_available_seats(flight)
        
        for seat in available_seats:
            classes[seat.seatClass].append(seat.number)
        
        for seat_class, seats in classes.items():
            if seats:
                print(f"\n🏆 {seat_class}: {len(seats)} disponíveis")
                # Mostrar apenas os primeiros 10 para não poluir
                seats_to_show = seats[:10]
                print(f"   Assentos: {', '.join(seats_to_show)}")
                if len(seats) > 10:
                    print(f"   ... e mais {len(seats) - 10} assentos")

    def check_reservation(self):
        """Consulta uma reserva existente."""
        self.clear_screen()
        print("🔍 CONSULTAR RESERVA")
        print("="*30)
        
        booking_code = input("Digite o código da reserva: ")
        
        reservation = self._booking_system.get_booking(booking_code)
        
        if reservation:
            print(f"\n✅ Reserva encontrada:")
            print(f"🎫 Código: {booking_code}")
            print(f"✈️  Voo: {reservation['flight'].flight_id}")
            print(f"🛫 Origem: {reservation['flight'].origin}")
            print(f"🛬 Destino: {reservation['flight'].destination}")
            print(f"💺 Assento: {reservation['seat'].number}")
            print(f"🏆 Classe: {reservation['seat'].seatClass}")
            print(f"👤 Passageiro: {reservation['passenger'].name}")
            print(f"📅 Data da reserva: {reservation['booking_date'].strftime('%d/%m/%Y %H:%M')}")
            print(f"📊 Status: {reservation['status']}")
        else:
            print("❌ Reserva não encontrada!")
        
        input("\nPressione Enter para continuar...")

    def cancel_reservation(self):
        """Cancela uma reserva existente."""
        self.clear_screen()
        print("❌ CANCELAR RESERVA")
        print("="*30)
        
        booking_code = input("Digite o código da reserva: ")
        
        if self._booking_system.cancel_booking(booking_code):
            print("✅ Reserva cancelada com sucesso!")
        else:
            print("❌ Reserva não encontrada!")
        
        input("\nPressione Enter para continuar...")

    def show_available_flights(self):
        """Mostra todos os voos com assentos disponíveis."""
        self.clear_screen()
        print("✈️  VOOS DISPONÍVEIS")
        print("="*50)
        
        for flight in self._flights:
            available_seats = self._booking_system.get_available_seats(flight)
            
            if available_seats:
                print(f"\n🛫 {flight.get_info()}")
                print(f"   💺 {len(available_seats)} assentos disponíveis")
                
                # Contar por classe
                classes_count = {}
                for seat in available_seats:
                    classes_count[seat.seatClass] = classes_count.get(seat.seatClass, 0) + 1
                
                for seat_class, count in classes_count.items():
                    print(f"   🏆 {seat_class}: {count} assentos")
        
        input("\nPressione Enter para continuar...")

    def show_statistics(self):
        """Mostra estatísticas do sistema."""
        self.clear_screen()
        print("📊 ESTATÍSTICAS DO SISTEMA")
        print("="*40)
        
        stats = self._booking_system.get_booking_statistics()
        
        print(f"\n📈 Reservas totais: {stats['total_bookings']}")
        print(f"✅ Reservas ativas: {stats['active_bookings']}")
        print(f"❌ Reservas canceladas: {stats['cancelled_bookings']}")
        
        # Estatísticas por voo
        print(f"\n✈️  Estatísticas por Voo:")
        for flight in self._flights:
            total_seats = len(flight.seats)
            available_seats = len(self._booking_system.get_available_seats(flight))
            occupied_seats = total_seats - available_seats
            occupancy_rate = (occupied_seats / total_seats) * 100
            
            print(f"   {flight.flight_id}: {occupied_seats}/{total_seats} ({occupancy_rate:.1f}%)")
        
        input("\nPressione Enter para continuar...")
