import random
from datetime import datetime
from typing import Dict, Optional
from Entities.Flight import Flight
from Entities.Passenger import Passenger
from Entities.Seat import Seat
from Entities.PlaneTicket import PlaneTicket


class BookingSystem:
    """
    Sistema de reservas responsável por gerenciar todas as operações de booking.
    Segue o princípio Single Responsibility - apenas cuida das reservas.
    """
    
    def __init__(self):
        self._tickets: Dict[str, PlaneTicket] = {}
        self._booking_counter = 100000

    def book_seat(self, flight: Flight, seat_number: str, passenger: Passenger) -> str:
        """
        Faz uma reserva completa de assento.
        
        Args:
            flight: Voo onde será feita a reserva
            seat_number: Número do assento desejado
            passenger: Passageiro que fará a reserva
            
        Returns:
            Código de reserva gerado
            
        Raises:
            ValueError: Se o assento não existir ou já estiver reservado
        """
        seat = flight.get_seat(seat_number)
        
        if not seat:
            raise ValueError(f"Assento {seat_number} não encontrado.")
        
        if seat.is_reserved():
            raise ValueError(f"Assento {seat_number} já está reservado.")
        
        # Gera código de reserva único
        booking_code = self.generate_booking_code()
        
        # Efetua a reserva
        seat.assign_passenger(passenger)
        
        # Cria o bilhete
        ticket = PlaneTicket(booking_code, flight, seat, passenger)
        self._tickets[booking_code] = ticket
        
        return booking_code

    def cancel_booking(self, booking_code: str) -> bool:
        """
        Cancela uma reserva existente.
        
        Args:
            booking_code: Código da reserva a ser cancelada
            
        Returns:
            True se cancelada com sucesso, False se não encontrada
        """
        if booking_code not in self._tickets:
            return False
        
        ticket = self._tickets[booking_code]
        ticket.cancel_ticket()
        
        return True

    def get_booking(self, booking_code: str) -> Optional[PlaneTicket]:
        """
        Recupera informações de uma reserva.
        
        Args:
            booking_code: Código da reserva
            
        Returns:
            Bilhete ou None se não encontrado
        """
        return self._tickets.get(booking_code)

    def get_available_seats(self, flight: Flight, seat_class: str = None) -> list[Seat]:
        """
        Retorna assentos disponíveis em um voo.
        
        Args:
            flight: Voo para verificar assentos
            seat_class: Classe específica (opcional)
            
        Returns:
            Lista de assentos disponíveis
        """
        available_seats = [seat for seat in flight.seats if not seat.is_reserved()]
        
        if seat_class:
            available_seats = [seat for seat in available_seats if seat.seatClass == seat_class]
        
        return available_seats

    def get_passenger_bookings(self, passenger_name: str) -> list[PlaneTicket]:
        """
        Retorna todas as reservas de um passageiro.
        
        Args:
            passenger_name: Nome do passageiro
            
        Returns:
            Lista de bilhetes do passageiro
        """
        passenger_tickets = []
        
        for ticket in self._tickets.values():
            if ticket.passenger.name == passenger_name and ticket.is_active():
                passenger_tickets.append(ticket)
        
        return passenger_tickets

    def generate_booking_code(self) -> str:
        """
        Gera um código de reserva único.
        
        Returns:
            Código de reserva no formato BK######
        """
        self._booking_counter += 1
        return f"BK{self._booking_counter}"

    def get_booking_statistics(self) -> Dict:
        """
        Retorna estatísticas do sistema de reservas.
        
        Returns:
            Dicionário com estatísticas
        """
        total_bookings = len(self._tickets)
        active_bookings = len([t for t in self._tickets.values() if t.is_active()])
        cancelled_bookings = len([t for t in self._tickets.values() if not t.is_active()])
        
        return {
            'total_bookings': total_bookings,
            'active_bookings': active_bookings,
            'cancelled_bookings': cancelled_bookings
        }
