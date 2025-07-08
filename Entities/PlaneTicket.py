from datetime import datetime
from typing import Optional
from Entities.Flight import Flight
from Entities.Passenger import Passenger
from Entities.Seat import Seat


class PlaneTicket:
    """
    Representa um bilhete de avião com todas as informações da reserva.
    """
    
    def __init__(self, booking_code: str, flight: Flight, seat: Seat, passenger: Passenger):
        self._booking_code = booking_code
        self._flight = flight
        self._seat = seat
        self._passenger = passenger
        self._booking_date = datetime.now()
        self._status = "CONFIRMADO"
    
    @property
    def booking_code(self) -> str:
        return self._booking_code
    
    @property
    def flight(self) -> Flight:
        return self._flight
    
    @property
    def seat(self) -> Seat:
        return self._seat
    
    @property
    def passenger(self) -> Passenger:
        return self._passenger
    
    @property
    def booking_date(self) -> datetime:
        return self._booking_date
    
    @property
    def status(self) -> str:
        return self._status
    
    def cancel_ticket(self):
        """Cancela o bilhete."""
        self._status = "CANCELADO"
        self._seat.release_seat()
    
    def is_active(self) -> bool:
        """Verifica se o bilhete está ativo."""
        return self._status == "CONFIRMADO"
    
    def __str__(self) -> str:
        return (f"Bilhete {self._booking_code} - "
                f"Voo: {self._flight.flight_id} - "
                f"Assento: {self._seat.number} - "
                f"Passageiro: {self._passenger.name} - "
                f"Status: {self._status}")
