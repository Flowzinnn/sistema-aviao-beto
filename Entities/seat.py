class Seat:
    """
    Representa um assento em um avião.
    
    Args:
        Number: O número do assento.
        SeatClass: A classe do assento (econômica, executiva, etc.).
    """
    def __init__(self, number: str, seatClass: str):
        self._number = number
        self._seatClass = seatClass
        self._reserved = False
        self._passenger = None

    @property
    def number(self):
        return self._number

    @property
    def seatClass(self):
        return self._seatClass

    @property
    def reserved(self):
        return self._reserved

    def reserve(self, passenger):
        """
        Reserva o assento para um passageiro.
        """
        if self._reserved:
            raise ValueError(f"Assento {self._number} já está reservado.")
        self._passenger = passenger
        self._reserved = True

    def get_passenger(self):
        return self._passenger

    def __str__(self):
        status = "X" if self._reserved else "Livre"
        return f"Assento {self._number} - {status}"
