from Entities.DefaultPeople import DefaultPeople

class Passenger(DefaultPeople):
    """
    Representa um passageiro no sistema de voos.
    
    Herda de DefaultPeople e adiciona funcionalidades específicas para passageiros,
    como histórico de voos e métodos relacionados a viagens.
    
    Example:
        >>> passenger = Passenger("João Silva", "12345678900", 30)
        >>> passenger.name
        'João Silva'
        >>> passenger.type()
        'Passenger'
    """
    
    def __init__(self, name: str, CPF: int, age: int):
        super().__init__(name, CPF, age)

    @property
    def type(self) -> str:
        return "Passenger"