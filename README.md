# Sistema de Gerenciamento de Voos ✈️

Um sistema completo de gerenciamento de voos desenvolvido em Python, permitindo visualizar informações sobre voos, tripulação, assentos e realizar reservas de passagens.

## 📋 Funcionalidades

- **Gerenciamento de Voos**: Visualização de voos disponíveis com origem e destino
- **Sistema de Reservas**: Fazer, consultar e cancelar reservas de passagens
- **Informações da Tripulação**: Visualização completa do piloto, copiloto e comissários de bordo
- **Detalhes da Aeronave**: Informações sobre o modelo do avião utilizado
- **Sistema de Assentos**: Consulta de assentos específicos com diferentes classes (Primeira Classe, Executiva, Econômica)
- **Bilhetes Digitais**: Sistema de bilhetes com códigos únicos e status
- **Estatísticas**: Relatórios de ocupação e reservas do sistema
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
├── main.py                    # Arquivo principal (entry point)
├── menuAdmin.py               # Menu administrativo
├── MenuBooking.py             # Menu de reservas
├── BookingSystem.py           # Sistema de reservas
├── GeneratorFaker.py          # Geração de dados fictícios com Faker
├── README.md                  # Documentação do projeto
│
└── Entities/                  # Entidades do sistema
    ├── __init__.py
    ├── Enums.py               # Enums: SeatClass, AirplaneModel, CrewRole
    ├── Airplane.py            # Classe Airplane
    ├── CrewMember.py          # Classes Pilot, Copilot, FlightAttendant
    ├── DefaultPeople.py       # Classe abstrata DefaultPeople
    ├── Flight.py              # Classe Flight (voo)
    ├── Passenger.py           # Classe Passenger
    ├── Seat.py                # Classe Seat (assento)
    └── PlaneTicket.py         # Classe PlaneTicket (bilhete)
```

## 🎯 Exemplos de Uso

### Menu Principal

O sistema apresenta um menu principal simples onde você pode:
- Acessar o menu administrativo
- Acessar o sistema de reservas
- Sair do sistema

Exemplo de output:
```
MENU PRINCIPAL
1 - Menu Administrador
2 - Sistema de Reservas
0 - Sair
Digite sua opcao:
```

### Sistema de Reservas

O sistema de reservas permite:
- Fazer nova reserva
- Consultar reserva existente
- Cancelar reserva
- Ver voos disponíveis
- Ver estatísticas do sistema

Exemplo de output:
```
SISTEMA DE RESERVAS
1 - Fazer nova reserva
2 - Consultar reserva
3 - Cancelar reserva
4 - Ver voos disponiveis
5 - Estatisticas do sistema
0 - Voltar ao menu principal
Escolha uma opcao:
```

### Menu Administrativo

O menu administrativo permite:
- Ver voos disponíveis
- Consultar informações detalhadas dos voos

Exemplo de output:
```
MENU ADMINISTRADOR
1 - Ver voos disponiveis
0 - Voltar
Digite sua opcao:
```

### Lista de Voos Disponíveis

Exemplo de output:
```
VOOS DISPONIVEIS
FlightID:(5669) <> Voo de Rocha da Praia com destino à Barbosa <> Avião: Airbus A330
FlightID:(2234) <> Voo de Santos com destino à Nascimento do Campo <> Avião: Boeing 787 Dreamliner
FlightID:(8119) <> Voo de da Paz com destino à da Rosa <> Avião: Airbus A380
FlightID:(5634) <> Voo de da Luz de Goiás com destino à Oliveira de Minas <> Avião: Boeing 777
FlightID:(7625) <> Voo de das Neves com destino à da Paz <> Avião: Boeing 747
```

### Fazer Nova Reserva

Exemplo do processo de reserva:
```
NOVA RESERVA

Voos Disponiveis:
ID: 5669 | Rocha da Praia → Barbosa (Airbus A330) | 45 assentos livres

Digite o ID do voo: 5669

Assentos Disponiveis - Voo 5669:

Primeira Classe: 5 disponiveis
Assentos: 1, 2, 3, 4, 5

Executiva: 15 disponiveis
Assentos: 26, 27, 28, 29, 30, 31, 32, 33, 34, 35
... e mais 5 assentos

Dados do Passageiro:
Nome: João Silva
CPF: 123.456.789-00
Idade: 30

Numero do assento desejado: 1

RESERVA REALIZADA COM SUCESSO!
Codigo de reserva: BK100001
Voo: 5669
Assento: 1
Passageiro: João Silva
```

### Consultar Reserva

Exemplo de consulta:
```
CONSULTAR RESERVA
Digite o codigo da reserva: BK100001

RESERVA ENCONTRADA
Codigo: BK100001
Voo: 5669
Origem: Rocha da Praia
Destino: Barbosa
Assento: 1
Classe: Primeira Classe
Passageiro: João Silva
Data da reserva: 07/07/2025 14:30
Status: CONFIRMADO
```

### Menu do Voo Selecionado

Para cada voo no menu administrativo, você pode:
```
VOO 5669
1 - Ver tripulacao
2 - Ver modelo do aviao
3 - Ver assento especifico
0 - Voltar
Digite sua opcao:
```

### Informações da Tripulação

Exemplo de output:
```
TRIPULACAO DO VOO 5669
1 - Piloto: Dr. João Guilherme Costela
2 - Copiloto: Luiz Fernando Costa
3 - Comissario 1: Aylla Rezende
4 - Comissario 2: Maria Cecília Machado
0 - Voltar
Escolha um tripulante:
```

### Modelo do Avião

Exemplo de output:
```
Modelo do aviao: Airbus A330
```

### Consulta de Assento

Exemplo de output:
```
Assento: 1 | Classe: Primeira Classe | Passageiro: Ana Beatriz Pires
```

### Distribuição dos Assentos

O sistema possui assentos distribuídos em três classes baseado no modelo do avião:
- **Primeira Classe**: ~5-10% dos assentos (assentos premium)
- **Executiva**: ~15-20% dos assentos (assentos business)  
- **Econômica**: ~70-80% dos assentos (assentos padrão)

Exemplo para um Boeing 737 (189 assentos):
- **Primeira Classe**: 19 assentos
- **Executiva**: 38 assentos
- **Econômica**: 132 assentos

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

#### `PlaneTicket`
- Representa um bilhete de avião completo
- Atributos: código de reserva, voo, assento, passageiro, data, status
- Métodos: `cancel_ticket()`, `is_active()`, `__str__()`

#### `BookingSystem`
- Sistema completo de reservas
- Gerencia criação, consulta e cancelamento de bilhetes
- Trabalha com objetos `PlaneTicket` para melhor organização
- Métodos: `book_seat()`, `cancel_booking()`, `get_booking()`, `get_statistics()`

#### `Airplane`
- Representa uma aeronave
- Utiliza enum `AirplaneModel` para modelos disponíveis
- Atributos: modelo e capacidade

#### `Seat`
- Representa um assento no avião
- Pode ser reservado para um passageiro
- Possui classe do assento (Primeira Classe, Executiva, Econômica)
- Distribuição baseada no modelo do avião
- Métodos: `assign_passenger()`, `release_seat()`, `is_reserved()`

#### `Flight`
- Classe principal que gerencia um voo
- Contém: ID, origem, destino, avião, assentos, tripulação
- Gera automaticamente passageiros e tripulação usando GeneratorFaker
- Distribui assentos em diferentes classes automaticamente baseado no modelo do avião
- Usa mapa de assentos para busca O(1)

#### `GeneratorFaker`
- Classe responsável pela geração de dados fictícios
- Utiliza a biblioteca Faker para criar dados realistas
- Gera passageiros, tripulação, cidades e IDs únicos

#### `AdminMenu`
- Interface principal do sistema
- Gerencia navegação entre menus
- Controla interação com o usuário
- Menu administrativo simples e limpo

#### `BookingMenu`
- Interface do sistema de reservas
- Permite fazer, consultar e cancelar reservas
- Mostra estatísticas do sistema
- Interface simples e intuitiva

#### `Enums`
- **SeatClass**: Enum para classes de assento (Econômica, Executiva, Primeira Classe)
- **AirplaneModel**: Enum para modelos de aeronaves
- **CrewRole**: Enum para funções da tripulação

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Faker**: Biblioteca para geração de dados fictícios brasileiros
- **Enum**: Para modelagem de tipos de aeronaves e classes de assentos
- **ABC (Abstract Base Classes)**: Para classes abstratas
- **POO**: Aplicação completa de conceitos de Programação Orientada a Objetos

## 🔧 Funcionalidades Técnicas

### Funcionalidades Técnicas

### Sistema de Reservas Completo
- **Bilhetes Digitais**: Cada reserva gera um objeto `PlaneTicket` com código único
- **Códigos de Reserva**: Formato BK###### (ex: BK100001)
- **Status de Bilhetes**: CONFIRMADO ou CANCELADO
- **Consulta por Código**: Busca rápida de reservas
- **Cancelamento**: Liberação automática de assentos

### Capacidades Reais de Aviões
- **Boeing 737**: 189 assentos
- **Boeing 747**: 660 assentos
- **Boeing 777**: 396 assentos
- **Boeing 787**: 330 assentos
- **Airbus A320**: 180 assentos
- **Airbus A330**: 277 assentos
- **Airbus A350**: 350 assentos
- **Airbus A380**: 853 assentos

### Geração Automática de Dados
O sistema utiliza a biblioteca Faker configurada para o Brasil (pt_BR) para gerar:
- Nomes de passageiros e tripulantes brasileiros
- CPFs válidos no formato brasileiro
- Idades aleatórias apropriadas para cada tipo de pessoa
- Cidades brasileiras de origem e destino
- IDs únicos de voos de 4 dígitos

### Classes de Assentos
- **Primeira Classe**: ~5-10% dos assentos (baseado no modelo do avião)
- **Executiva**: ~15-20% dos assentos (baseado no modelo do avião)
- **Econômica**: ~70-80% dos assentos (baseado no modelo do avião)

### Arquitetura Orientada a Objetos
- Herança: `DefaultPeople` → `Passenger`, `CrewMember`
- Composição: `Flight` contém `Airplane`, `Seat[]`, `CrewMember[]`
- Agregação: `BookingSystem` gerencia `PlaneTicket[]`
- Enums: Para garantir type safety e constantes
- Properties: Encapsulamento com getters/setters pythônicos

### Performance e Otimizações
- **Busca O(1)**: Mapa de assentos para busca rápida
- **Objetos em vez de dicionários**: Melhor organização e type safety
- **Encapsulamento**: Responsabilidades bem definidas

### Modelos de Aeronaves Disponíveis
- **Boeing**: 737, 747, 777, 787 Dreamliner
- **Airbus**: A320, A330, A350, A380
- **Embraer**: E190, E195

### Validações e Segurança
- IDs de voos únicos (4 dígitos)
- Códigos de reserva únicos (formato BK######)
- Validação de entrada do usuário nos menus
- Verificação de assentos existentes
- Prevenção de reservas duplicadas
- Mensagens de erro padronizadas com prefixo [ERRO]

### Interface do Usuário
- **Design Simples**: Menus básicos sem decorações excessivas
- **Navegação Intuitiva**: Prompts claros e diretos
- **Feedback Claro**: Mensagens de sucesso e erro bem definidas
- **Consistency**: Padrão visual consistente em todos os menus

### Padrões de Código
- **PascalCase**: Para nomes de classes (`Flight`, `GeneratorFaker`)
- **camelCase**: Para métodos e propriedades (`generateSeats`, `seatClass`)
- **snake_case**: Para atributos privados (`_flight_id`, `_seats`)
- **Type Hints**: Para melhor documentação e IDE support

## 👥 Contribuição

Este projeto foi desenvolvido como trabalho acadêmico do IFMS (Instituto Federal de Mato Grosso do Sul) para a disciplina de Paradigma Orientado a Objetos.

## 📄 Licença

Este projeto é desenvolvido para fins educacionais.

---

**Desenvolvido por**: Nicolas Wolf  
**Instituição**: IFMS - Instituto Federal de Mato Grosso do Sul  
**Disciplina**: Paradigma Orientado a Objetos  
**Ano**: 2025
