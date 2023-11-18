from itertools import product

# Lista zawierająca liczby lub ciągi znaków
elements = ["Ada", "Adalbert", "Adam", "Adela", "Adelajda", "Adrian", "Aga", "Agata", "Agnieszka", "Albert", "Alberta", "Aldona", "Aleksander", "Aleksandra", "Alfred", "Alicja", "Alina", "Amadeusz", "Ambroży", "Amelia", "Anastazja", "Anastazy", "Anatol", "Andrzej", "Aneta", "Angelika", "Angelina", "Aniela", "Anita", "Anna", "Antoni", "Antonina", "Anzelm", "Apolinary", "Apollo", "Apolonia", "Apoloniusz", "Ariadna", "Arkadiusz", "Arkady", "Arlena", "Arleta", "Arletta", "Arnold", "Arnolf", "August", "Augustyna", "Aurela", "Aurelia", "Aurelian", "Aureliusz", "Balbina", "Baltazar", "Barbara", "Bartłomiej", "Bartosz", "Bazyli", "Beata", "Benedykt", "Benedykta", "Beniamin", "Bernadeta", "Bernard", "Bernardeta", "Bernardyn", "Bernardyna", "Błażej", "Bogdan", "Bogdana", "Bogna", "Bogumił", "Bogumiła", "Bogusław", "Bogusława", "Bohdan", "Bolesław", "Bonawentura", "Bożena", "Bronisław", "Broniszław", "Bronisława", "Brunon", "Brygida", "Cecyl", "Cecylia", "Celestyn", "Celestyna", "Celina", "Cezary", "Cyprian", "Cyryl", "Dalia", "Damian", "Daniel", "Daniela", "Danuta", "Daria", "Dariusz", "Dawid", "Diana", "Dianna", "Dobrawa", "Dominik", "Dominika", "Donata", "Dorian", "Dorota", "Dymitr", "Edmund", "Edward", "Edwin", "Edyta", "Egon", "Eleonora", "Eliasz", "Eligiusz", "Eliza", "Elwira", "Elżbieta", "Emanuel", "Emanuela", "Emil", "Emilia", "Emilian", "Emiliana", "Ernest", "Ernestyna", "Erwin", "Erwina", "Eryk", "Eryka", "Eugenia", "Eugeniusz", "Eulalia", "Eustachy", "Ewelina", "Fabian", "Faustyn", "Faustyna", "Felicja", "Felicjan", "Felicyta", "Feliks", "Ferdynand", "Filip", "Franciszek", "Franciszek", "Salezy", "Franciszka", "Fryderyk", "Fryderyka", "Gabriel", "Gabriela",
            "Gaweł", "Genowefa", "Gerard", "Gerarda", "Gerhard", "Gertruda", "Gerwazy", "Godfryd", "Gracja", "Gracjan", "Grażyna", "Greta", "Grzegorz", "Gustaw", "Gustawa", "Gwidon", "Halina", "Hanna", "Helena", "Henryk", "Henryka", "Herbert", "Hieronim", "Hilary", "Hipolit", "Honorata", "Hubert", "Ida", "Idalia", "Idzi", "Iga", "Ignacy", "Igor", "Ildefons", "Ilona", "Inga", "Ingeborga", "Irena", "Ireneusz", "Irma", "Irmina", "Irwin", "Ismena", "Iwo", "Iwona", "Izabela", "Izolda", "Izyda", "Izydor", "Jacek", "Jadwiga", "Jagoda", "Jakub", "Jan", "Janina", "January", "Janusz", "Jarema", "Jarogniew", "Jaromir", "Jarosław", "Jarosława", "Jeremi", "Jeremiasz", "Jerzy", "Jędrzej", "Joachim", "Joanna", "Jolanta", "Jonasz", "Jonatan", "Jowita", "Józef", "Józefa", "Józefina", "Judyta", "Julia", "Julian", "Julianna", "Julita", "Juliusz", "Justyn", "Justyna", "Kacper", "Kaja", "Kajetan", "Kalina", "Kamil", "Kamila", "Karina", "Karol", "Karolina", "Kacper", "Kasper", "Katarzyna", "Kazimiera", "Kazimierz", "Kinga", "Klara", "Klarysa", "Klaudia", "Klaudiusz", "Klaudyna", "Klemens", "Klementyn", "Klementyna", "Kleopatra", "Klotylda", "Konrad", "Konrada", "Konstancja", "Konstanty", "Konstantyn", "Kordelia", "Kordian", "Kordula", "Kornel", "Kornelia", "Kryspin", "Krystian", "Krystyn", "Krystyna", "Krzysztof", "Ksenia", "Kunegunda", "Laura", "Laurenty", "Laurentyn", "Laurentyna", "Lech", "Lechosław", "Lechosława", "Leokadia", "Leon", "Leonard", "Leonarda", "Leonia", "Leopold", "Leopoldyna", "Lesław", "Lesława", "Leszek", "Lidia", "Ligia", "Lilian", "Liliana", "Lilianna", "Lilla", "Liwia", "Liwiusz", "Liza", "Lolita", "Longin", "Loretta", "Luba", "Lubomir", "Lubomira", "Lucja", ]

# Długości kombinacji
combination_lengths = [1, 2, 3]
all_combinations = []

# Generowanie wszystkich możliwych kombinacji dla różnych długości
for length in combination_lengths:
    combinations = list(product(elements, repeat=length))
    all_combinations.append(combinations)

# Wyświetlenie wszystkich kombinacji
print("---------------------------------------------------------------")
for i, combinations in enumerate(all_combinations, start=1):
    print(f"Kombinacje o długości {i}:")
    for combination in combinations:
        combined = ''.join(str(elem) for elem in combination)
        print(combined)
    print()
