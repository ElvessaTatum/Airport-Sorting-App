from airports_data import airports
from fetch_criteria import fetch_criteria, fetch_a_criterion
from process_airports import process_airports
import os

def console_application():
    def display_available_criteria():
        print("0. No Sort")
        for index, criteria in enumerate(fetch_criteria(), start=1):
            print(f"{index}. {criteria.title()}")

    def get_user_input():
        while True:
            user_input = int(input(f"Enter your choice (0-{len(fetch_criteria())}): "))
            if 0 <= user_input <= len(fetch_criteria()):
                return user_input
            print(f"Error: Input must be an integer between 0 and {len(fetch_criteria())}. Please try again.")

    def handle_user_input(user_input):
        if user_input == 0:
            return lambda airport: ()
        else:
            criteria = fetch_criteria()[user_input - 1]
            return fetch_a_criterion(criteria)

    def format_airports(airport):
        airport_info = ', '.join([f'"{information}"' if isinstance(information, str) else str(information) for information in vars(airport).values()])
        return f'Airport({airport_info})'

    def display_airports(airports_list):
        for airport in airports_list:
            print(format_airports(airport))

    display_available_criteria()

    user_input = get_user_input()
    sort_type = handle_user_input(user_input)
    sorted_airports = process_airports(airports, sort_type)

    print("\nResult Airport List:\n")
    display_airports(sorted_airports)

def main():
    print("Welcome to the Airport Sorting Program!")
    print("List of available sort criteria:")

    console_application()

if __name__ == "__main__":
    os.chdir('src')
    main()
