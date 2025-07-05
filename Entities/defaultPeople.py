from abc import ABC, abstractmethod

class DefaultPeople(ABC):
    """
    Inicializa uma pessoa padrão.
    
    Args:
        name (str): Nome da pessoa.
        CPF (int): CPF da pessoa.
        age (int): Idade da pessoa.
    """
    def __init__(self, name: str, CPF: int, age: int):
        self._name = name
        self._CPF = CPF
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def CPF(self):
        return self._CPF

    @CPF.setter
    def CPF(self, value):
        self._CPF = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        
    @abstractmethod
    def type(self) -> str:
        """
        Retorna o tipo da pessoa (ex: Cliente, Tripulante).
        """
        pass