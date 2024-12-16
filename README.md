
# Python Pokédex Searcher

## Overview
This is a beginner-friendly Python project: a simple Pokédex search tool. It uses the **PokéAPI** to fetch and display data about any Pokémon by its name or Pokédex number. The project demonstrates fundamental Python concepts and introduces interacting with RESTful APIs.

## Features
- Allows users to:
  - Search for any Pokémon by name or Pokédex number.
  - View detailed information about the Pokémon, including:
    - Name
    - Types
    - Abilities
  - Receive feedback if the entered Pokémon name/number is invalid.
- Demonstrates key Python concepts:
  - **Loops**: Continuous input prompts using a `while` loop.
  - **APIs**: Making HTTP requests with the `requests` library.
  - **JSON parsing**: Extracting and displaying relevant information from API responses.
  - **String manipulation**: Normalizing input to be case-insensitive.
  - **Conditional statements**: Handling success and error responses from the API.

## What I Learned
- How to interact with REST APIs using the `requests` library.
- Parsing JSON data to extract specific details.
- Leveraging loops for continuous user interaction.
- Using conditional statements to handle errors and edge cases.
- String formatting with f-strings to display information in a readable format.

## Example Usage
```text
Search Pokédex: pikachu
Name is    pikachu
Type:
electric
Abilities:
static
lightning-rod

Search Pokédex: charizard
Name is    charizard
Type:
fire
flying
Abilities:
blaze
solar-power

Search Pokédex: invalidname
Pokémon Not Found
```

## How to Run
1. Ensure you have **Python 3.9+** installed on your system. You can download it from [python.org](https://python.org).
2. Save the `pokedex.py` file on your computer.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the program using the command:
   ```bash
   python pokedex.py
   ```

## Credits
This project was inspired by the Python section of the [Ultimate 2024 Fullstack Web Development Bootcamp](https://www.udemy.com/course/the-ultimate-fullstack-web-development-bootcamp/) on Udemy. Special thanks to the instructor **Kalob Taulien** for providing an excellent learning foundation. Additionally, the Pokémon data is sourced from the [PokéAPI](https://pokeapi.co/).
