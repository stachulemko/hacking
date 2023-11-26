from itertools import product

# Lista zawierająca liczby lub ciągi znaków
elements = ["ania", "kowalska", 1, 2, "_", "salamalekum", "kepka", "błaszczyk"]

# Długości kombinacji
combination_lengths = [1, 2, 3]

# Generowanie wszystkich możliwych kombinacji dla różnych długości
with open('C:\\tmp\\all_combinations.txt', 'w') as file:
    for length in combination_lengths:
        combinations = list(product(elements, repeat=length))
        file.write(f"Kombinacje o długości {length}:\n")
        for combination in combinations:
            combined = ''.join(str(elem) for elem in combination)
            file.write(f"{combined}\n")
            print(combined)
        file.write("\n\n")
        print("\n---------------------------------------------------------------\n")
