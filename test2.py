from itertools import product

# Lista zawierająca liczby lub ciągi znaków
elements = ["ania", "kowalska", 1, 2, "_", "salamalekum", "kepka", "błaszczyk"]

# Długości kombinacji
combination_lengths = [1, 2, 3]
#all_combinations = []

# Generowanie wszystkich możliwych kombinacji dla różnych długości
for length in combination_lengths:
    combinations = list(product(elements, repeat=length))
    # all_combinations.append(combinations)
    with open('c:\\tmp\\not_ready.txt', 'r') as file:
        file.write(f"{combinations}")

# Wyświetlenie wszystkich kombinacji
""" print("---------------------------------------------------------------")
for i, combinations in enumerate(all_combinations, start=1):
    print(f"Kombinacje o długości {i}:")
    for combination in combinations:
        combined = ''.join(str(elem) for elem in combination)
        print(combined)
    print() """
