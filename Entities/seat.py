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

    def is_reserved(self) -> bool:
        """
        Verifica se o assento está reservado.
        
        Returns:
            True se reservado, False caso contrário
        """
        return self._reserved

    def assign_passenger(self, passenger):
        """
        Atribui um passageiro ao assento (método interno usado pelo BookingSystem).
        
        Args:
            passenger: Passageiro a ser atribuído
        """
        self._passenger = passenger
        self._reserved = True

    def release_seat(self):
        """
        Libera o assento (método interno usado pelo BookingSystem).
        """
        self._passenger = None
        self._reserved = False

    def get_passenger(self):
        """
        Retorna o passageiro do assento.
        
        Returns:
            Passageiro atribuído ao assento ou None se livre
        """
        return self._passenger

    def __str__(self):
        status = "X" if self._reserved else "Livre"
        return f"Assento {self._number} - {status}"
