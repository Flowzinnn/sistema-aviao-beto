import random
from datetime import datetime
from typing import Dict, Optional
from Entities.Flight import Flight
from Entities.Passenger import Passenger
from Entities.Seat import Seat


class BookingSystem:
    """
    Sistema de reservas responsável por gerenciar todas as operações de booking.
    Segue o princípio Single Responsibility - apenas cuida das reservas.
    """
    
    def __init__(self):
        self._reservations: Dict[str, Dict] = {}
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
        
        # Armazena informações da reserva
        self._reservations[booking_code] = {
            'flight': flight,
            'seat': seat,
            'passenger': passenger,
            'booking_date': datetime.now(),
            'status': 'CONFIRMADO'
        }
        
        return booking_code

    def cancel_booking(self, booking_code: str) -> bool:
        """
        Cancela uma reserva existente.
        
        Args:
            booking_code: Código da reserva a ser cancelada
            
        Returns:
            True se cancelada com sucesso, False se não encontrada
        """
        if booking_code not in self._reservations:
            return False
        
        reservation = self._reservations[booking_code]
        seat = reservation['seat']
        
        # Libera o assento
        seat._release_seat()
        
        # Atualiza status da reserva
        reservation['status'] = 'CANCELADO'
        
        return True

    def get_booking(self, booking_code: str) -> Optional[Dict]:
        """
        Recupera informações de uma reserva.
        
        Args:
            booking_code: Código da reserva
            
        Returns:
            Dicionário com informações da reserva ou None se não encontrada
        """
        return self._reservations.get(booking_code)

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

    def get_passenger_bookings(self, passenger_name: str) -> list[Dict]:
        """
        Retorna todas as reservas de um passageiro.
        
        Args:
            passenger_name: Nome do passageiro
            
        Returns:
            Lista de reservas do passageiro
        """
        passenger_bookings = []
        
        for booking_code, reservation in self._reservations.items():
            if reservation['passenger'].name == passenger_name and reservation['status'] == 'CONFIRMADO':
                passenger_bookings.append({
                    'booking_code': booking_code,
                    'flight_id': reservation['flight'].flight_id,
                    'seat_number': reservation['seat'].number,
                    'seat_class': reservation['seat'].seatClass,
                    'booking_date': reservation['booking_date']
                })
        
        return passenger_bookings

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
        total_bookings = len(self._reservations)
        active_bookings = len([r for r in self._reservations.values() if r['status'] == 'CONFIRMADO'])
        cancelled_bookings = len([r for r in self._reservations.values() if r['status'] == 'CANCELADO'])
        
        return {
            'total_bookings': total_bookings,
            'active_bookings': active_bookings,
            'cancelled_bookings': cancelled_bookings
        }
