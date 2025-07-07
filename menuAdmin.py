from Entities.flight import Flight
from generatorFaker import generate_city_pair, generate_flight_id
import os

flights = []
existing_ids = set()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_admin_menu():
    global flights, existing_ids
    for _ in range(10):
        origin, destination = generate_city_pair()
        flight_id = generate_flight_id(existing_ids)
        existing_ids.add(flight_id)
        flights.append(Flight(flight_id, origin, destination))

    clear_screen()
    main_menu()
    
def main_menu():
    while True:
        print("=== Menu Administrador ===")
        print("1 - Ver voos disponíveis")
        print("0 - Sair")
        option = input("Escolha uma opção: ")

        if option == "1":
            clear_screen()
            select_flight()
        elif option == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

def select_flight():
    print("=== Voos Disponíveis ===")
    for flight in flights:
        print(flight.get_info())

    selected_id = input("\nDigite o ID do voo que deseja visualizar: ")
    selected_flight = next((f for f in flights if f.flight_id == selected_id), None)

    if selected_flight:
        flight_menu(selected_flight)
    else:
        print("Voo não encontrado.")

def flight_menu(flight):
    while True:
        print(f"\n=== Voo {flight.flight_id} ===")
        print("1 - Ver tripulação")
        print("2 - Ver modelo do avião")
        print("3 - Ver assento específico")
        print("0 - Voltar")

        option = input("Escolha uma opção: ")

        if option == "1":
            crew = flight.get_crew()
            print(f"\nPiloto: {crew['Piloto'].name}")
            print(f"Copiloto: {crew['Copiloto'].name}")
            for i, attendant in enumerate(crew["Comissários"], start=1):
                print(f"Comissário {i}: {attendant.name}")
        elif option == "2":
            print(f"\nModelo do avião: {flight.get_airplane_model()}")
        elif option == "3":
            number = input("Digite o número do assento: ")
            seat = flight.get_seat(number)
            if seat:
                passenger = seat.get_passenger()
                print(f"FlightID: {flight.flight_id} | Assento: {seat.number} | Classe: {seat.seatClass} | Passageiro: {passenger.name}")
            else:
                print("Assento não encontrado.")
        elif option == "0":
            clear_screen()
            break
        else:
            print("Opção inválida.")

