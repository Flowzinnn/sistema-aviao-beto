# Sistema de Gerenciamento de Voos ✈️

Um sistema completo de gerenciamento de voos desenvolvido em Python, permitindo visualizar informações sobre voos, tripulação, assentos e passageiros.

## 📋 Funcionalidades

- **Gerenciamento de Voos**: Visualização de voos disponíveis com origem e destino
- **Informações da Tripulação**: Visualização completa do piloto, copiloto e comissários de bordo
- **Detalhes da Aeronave**: Informações sobre o modelo do avião utilizado
- **Sistema de Assentos**: Consulta de assentos específicos e seus passageiros
- **Geração Automática de Dados**: Criação automática de voos, passageiros e tripulação usando dados fictícios

## 🚀 Como Executar

1. **Instale as dependências**:
```bash
pip install faker
```

2. **Execute o sistema**:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
sistema-aviao-beto/
│
├── main.py                    # Arquivo principal com interface do usuário
├── generatorFaker.py          # Geração de dados fictícios
├── README.md                  # Documentação do projeto
│
└── Entities/                  # Entidades do sistema
    ├── __init__.py
    ├── airplane.py            # Classe Airplane e enum AirplaneModel
    ├── crewMember.py          # Classes Pilot, Copilot, FlightAttendant
    ├── defaultPeople.py       # Classe abstrata DefaultPeople
    ├── flight.py              # Classe Flight (voo)
    ├── passenger.py           # Classe Passenger
    └── seat.py                # Classe Seat (assento)
```

## 🎯 Exemplos de Uso

### Menu Principal


O sistema apresenta um menu administrativo onde você pode:
- Ver voos disponíveis
- Sair do sistema

Exemplo de output:
```
=== Menu Administrador ===
1 - Ver voos disponíveis
0 - Sair
```

### Lista de Voos Disponíveis


Exemplo de output:
```
=== Voos Disponíveis ===
5669 - Rocha da Praia → Barbosa (Airbus A330)
2234 - Santos → Nascimento do Campo (Boeing 787 Dreamliner)
8119 - da Paz → da Rosa (Airbus A380)
5634 - da Luz de Goiás → Oliveira de Minas (Boeing 777)
7625 - das Neves → da Paz (Boeing 747)
6040 - Freitas da Mata → Rodrigues do Galho (Boeing 777)
3401 - Mendonça → da Mata de Minas (Boeing 747)
2902 - Moura → Martins (Airbus A320)
2184 - Vargas → Gomes (Airbus A380)
8889 - Cirino de Guerra → Ramos (Airbus A320)
```

### Menu do Voo Selecionado


Para cada voo, você pode:
1. Ver tripulação
2. Ver modelo do avião  
3. Ver assento específico
0. Voltar

### Informações da Tripulação


Exemplo de output:
```
=== Voo 5669 ===
Piloto: Dr. João Guilherme Costela
Copiloto: Luiz Fernando Costa
Comissário 1: Aylla Rezende
Comissário 2: Maria Cecília Machado
```

### Modelo do Avião

Exemplo de output:
```
=== Voo 5669 ===
Modelo do avião: Airbus A330
```

### Consulta de Assento

Exemplo de output:
```
=== Voo 5669 ===
FlightID: 5669 | Assento: 245 | Passageiro: Ana Beatriz Pires
```

## 🏗️ Arquitetura do Sistema

### Classes Principais

#### `DefaultPeople` (Classe Abstrata)
- Classe base para todas as pessoas no sistema
- Atributos: nome, CPF, idade
- Método abstrato: `type()`

#### `Passenger`
- Herda de `DefaultPeople`
- Representa um passageiro
- Possui histórico de voos

#### `CrewMember`
- Classe base para tripulantes
- Subclasses: `Pilot`, `Copilot`, `FlightAttendant`

#### `Airplane`
- Representa uma aeronave
- Utiliza enum `AirplaneModel` para modelos disponíveis
- Atributos: modelo e capacidade

#### `Seat`
- Representa um assento no avião
- Pode ser reservado para um passageiro
- Possui classe do assento (Econômica, etc.)

#### `Flight`
- Classe principal que gerencia um voo
- Contém: ID, origem, destino, avião, assentos, tripulação
- Gera automaticamente passageiros e tripulação

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Faker**: Biblioteca para geração de dados fictícios
- **Enum**: Para modelagem de tipos de aeronaves
- **ABC (Abstract Base Classes)**: Para classes abstratas

## 🔧 Funcionalidades Técnicas

### Geração Automática de Dados
O sistema utiliza a biblioteca Faker para gerar:
- Nomes de passageiros e tripulantes
- CPFs válidos
- Idades aleatórias
- Cidades de origem e destino
- IDs únicos de voos

### Modelos de Aeronaves Disponíveis
- Boeing 737, 747, 777, 787 Dreamliner
- Airbus A320, A330, A350, A380
- Embraer E190, E195

### Validações
- IDs de voos únicos
- Validação de entrada do usuário

## 👥 Contribuição

Este projeto foi desenvolvido como trabalho acadêmico do IFMS (Instituto Federal de Mato Grosso do Sul) para a disciplina de Paradigma Orientado a Objetos.

## 📄 Licença

Este projeto é desenvolvido para fins educacionais.

---

**Desenvolvido por**: Nicolas Wolf  
**Instituição**: IFMS - Instituto Federal de Mato Grosso do Sul  
**Disciplina**: Paradigma Orientado a Objetos  
**Ano**: 2025
