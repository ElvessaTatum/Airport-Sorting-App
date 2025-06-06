# Airport-Sorting-App
A console-based application that sorts and displays airport data based on user-selected criteria. Created by Elvessa Tatum and Dang Pham.

# Overview
This application demonstrates clean software architecture principles by providing a flexible airport data sorting system. Users can sort a collection of major US airports by various criteria including IATA codes, names, cities, states, delay status, and temperature. The system is designed for easy extensibility - new sorting criteria can be added without modifying existing code.

# Prerequisites
Python 3.7 or higher
No external dependencies required (uses only Python standard library)

# Features

Interactive Console Interface - User-friendly menu system with input validation
Multiple Sorting Options - 7 different sorting criteria available
Dynamic Criteria Discovery - Automatically detects available sorting options
Extensible Architecture - Add new sorting criteria without code changes
Data Formatting - Airport names displayed in uppercase, other data in original case
Error Handling - Robust input validation and exception handling
Modular Design - Clean separation of concerns across components

# Setup

1. Clone or download the project files
2. Ensure proper directory structure:
project/
├── src/
│   ├── airport.py
│   ├── airports_data.py
│   ├── fetch_criteria.py
│   ├── process_airports.py
│   ├── process_airports_UI.py
│   └── sort_criteria/
│       ├── criteria_for_sort_city.py
│       ├── criteria_for_sort_city_and_name.py
│       ├── criteria_for_sort_delay.py
│       ├── criteria_for_sort_iata.py
│       ├── criteria_for_sort_name.py
│       ├── criteria_for_sort_state.py
│       └── criteria_for_sort_temperature.py

3. Navigate to the project directory
4. Run the application:
    bashpython src/process_airports_UI.py

# Design Overview
Core Data Models – airport.py & airports_data.py

Airport dataclass with IATA code, name, city, state, temperature, and delay status
Static airport data collection with 7 major US airports

Backend Processing – process_airports.py

process_airports() – main processing function that applies sorting and formatting
uppercase_airport_name() – converts airport names to uppercase for display
Maintains data integrity while applying transformations

Dynamic Criteria System – fetch_criteria.py & sort_criteria/

fetch_criteria() – dynamically discovers available sorting options from filesystem
fetch_a_criterion() – loads specific sorting functions using dynamic imports
Modular criteria modules in sort_criteria/ directory for extensibility
Each criterion module contains a criteria_for_sort() function that returns sort key

Frontend – process_airports_UI.py

Console interface with numbered menu of sorting options
Input validation and error handling
Formatted output display with proper data representation
User-friendly prompts and result presentation

