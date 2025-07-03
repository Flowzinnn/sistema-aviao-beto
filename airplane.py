class Airplane:
    """
    Representa um modelo de avião.
    """
    def _init_(self, model: str, base_price: float):
        self._model = model
        self._base_price = base_price

    @property
    def model(self) -> str:
        """Retorna o nome do modelo do avião."""
        return self._model

    @property
    def base_price(self) -> float:
        """Retorna o preço base do modelo do avião."""
        return self._base_price

    def _str_(self) -> str:
        return f"Modelo: {self._model} | Preço base: R${self._base_price:.2f}"