class Seat:
    """
    Representa um assento em um voo.
    """
    def _init_(self, number: str, seat_class: str):
        self._number = number
        self._seat_class = seat_class  # Classe do assento(Econômica, Executiva, Primeira Classe)
        self._reserved = False

    @property
    def number(self) -> str:
        """Retorna o número do assento."""
        return self._number

    @property
    def seat_class(self) -> str:
        return self._seat_class

    def is_reserved(self) -> bool:
        return self._reserved

    def reserve(self) -> None:
        if self._reserved:
            raise ValueError(f"Assento {self._number} já está reservado.")
        self._reserved = True

    def _str_(self) -> str:
        status = "Reservado" if self._reserved else "Disponível"
        return f"Assento {self._number} ({self._seat_class}) - {status}"