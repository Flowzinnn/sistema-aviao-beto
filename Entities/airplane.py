from Entities.Enums import AirplaneModel

class Airplane:
    def __init__(self, model: AirplaneModel):
        self._model = model
        self._capacity = self.get_model_capacity(model)

    @property
    def model(self):
        """ Retorna o modelo do avião. """
        return self._model

    @property
    def capacity(self):
        """ Retorna a capacidade do avião baseada no modelo. """
        return self._capacity
    
    def get_model_capacity(self, model: AirplaneModel) -> int:
        """
        Retorna a capacidade baseada no modelo real do avião.
        
        Args:
            model: Modelo do avião
            
        Returns:
            Capacidade de passageiros do modelo
        """
        capacity_map = {
            AirplaneModel.BOEING_737: 180,
            AirplaneModel.BOEING_747: 450,
            AirplaneModel.BOEING_777: 350,
            AirplaneModel.BOEING_787: 290,
            AirplaneModel.AIRBUS_A320: 180,
            AirplaneModel.AIRBUS_A330: 300,
            AirplaneModel.AIRBUS_A350: 350,
            AirplaneModel.AIRBUS_A380: 550,
            AirplaneModel.EMBRAER_E190: 100,
            AirplaneModel.EMBRAER_E195: 120
        }
        return capacity_map.get(model, 250)  # Default 250 se modelo não encontrado
    
    def get_seat_distribution(self) -> dict:
        """
        Retorna a distribuição de assentos por classe baseada na capacidade.
        
        Returns:
            Dicionário com distribuição: {'first_class': int, 'executive': int, 'economic': int}
        """
        total_capacity = self._capacity
        
        # Distribuição percentual baseada no tamanho do avião
        if total_capacity <= 120:  # Aviões pequenos (Embraer)
            first_class = int(total_capacity * 0.05)  # 5%
            executive = int(total_capacity * 0.15)    # 15%
            economic = total_capacity - first_class - executive  # 80%
        elif total_capacity <= 200:  # Aviões médios (Boeing 737, A320)
            first_class = int(total_capacity * 0.08)  # 8%
            executive = int(total_capacity * 0.20)    # 20%
            economic = total_capacity - first_class - executive  # 72%
        else:  # Aviões grandes (Boeing 747, A380, etc)
            first_class = int(total_capacity * 0.10)  # 10%
            executive = int(total_capacity * 0.25)    # 25%
            economic = total_capacity - first_class - executive  # 65%
        
        return {
            'first_class': first_class,
            'executive': executive,
            'economic': economic
        }
