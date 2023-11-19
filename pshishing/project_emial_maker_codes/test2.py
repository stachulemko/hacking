from itertools import product

# Lista zawierająca liczby lub ciągi znaków
elements = ["ania", "kowalska", 1, 2, "_", "salamalekum", "kepka", "błaszczyk"]

# Długości kombinacji
combination_lengths = [1, 2, 3]
#all_combinations = []

# Generowanie wszystkich możliwych kombinacji dla różnych długości
with open('c:\\tmp\\not_ready.txt', 'w') as file:

    for length in combination_lengths:
        combinations = list(product(elements, repeat=length))
        print(f"{combinations}\n")
        # file.write(f"{combinations}\n")
    # all_combinations.append(combinations)


# Wyświetlenie wszystkich kombinacji
print("---------------------------------------------------------------")
for i, combinations in enumerate(all_combinations, start=1):
    print(f"Kombinacje o długości {i}:")
    for combination in combinations:
        combined = ''.join(str(elem) for elem in combination)
        print(combined)
    print()
