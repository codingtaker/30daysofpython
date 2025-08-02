 # Jour 11 : 30 Days of Python Programming

"""

Exercices 1:

"""

#1. Addition de deux nombres
def add_two_numbers(a, b):
    return a + b


# 2. Calcul de l’aire d’un cercle
import math

def area_of_circle(r):
    return math.pi * r * r

# 3. Somme de tous les éléments (arguments arbitraires)
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Tous les éléments doivent être numériques."


# 4. Convertisseur °C vers °F
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# 5. Déterminer la saison à partir du mois
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Mois invalide"


# 6. Calcul de la pente d’une équation linéaire y = mx + b
def calculate_slope(x1, y1, x2, y2):
    if x2 != x1:
        return (y2 - y1) / (x2 - x1)
    else:
        return "Division par zéro – pente indéfinie"


# 7. Résolution d’une équation quadratique
import cmath

def solve_quadratic_eqn(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    return (x1, x2)


# 8. Afficher les éléments d’une liste
def print_list(liste):
    for item in liste:
        print(item)


# 9. Inverser une liste avec une boucle

def reverse_list(liste):
    reversed_list = []
    for i in range(len(liste)-1, -1, -1):
        reversed_list.append(liste[i])
    return reversed_list


# 10. Mettre en majuscule les éléments d’une liste

def capitalize_list_items(liste):
    return [item.capitalize() for item in liste]


# 11. Ajouter un élément à une liste
def add_item(liste, item):
    liste.append(item)
    return liste


# 12. Supprimer un élément d’une liste
def remove_item(liste, item):
    if item in liste:
        liste.remove(item)
    return liste


# 13. Somme des nombres jusqu’à n inclus
def sum_of_numbers(n):
    return sum(range(n + 1))


# 14. Somme des nombres impairs jusqu’à n
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)


# 15. Somme des nombres pairs jusqu’à n
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)


"""

Exercices 2:

"""

#1.Fonction evens_and_odds(n) – Compter les pairs et impairs
print("Exercice N°2.1 : Compter les pairs et impairs")
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"Le nombre de pairs est {evens}.")
    print()
    print(f"Le nombre d'impairs est {odds}.")

evens_and_odds(100)
print()

# 2. Fonction factorial(n) – Factorielle
print("Exercice N°2.2 : Calcul de la factorielle")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


print(factorial(5))
print()
# 3. Fonction is_empty(x) – Vérifie si vide
print("Exercice N°2.3 : Vérification si vide")
def is_empty(param):
    if param:
        return False
    return True

print(is_empty(""))
print()
print(is_empty([1]))   

# 4. Fonctions statistiques
print("\nExercice N°2.4 : Fonctions statistiques")
data = [4, 2, 5, 8, 6, 9, 3, 4, 5]
def calculate_mean(lst):
    return sum(lst) / len(lst)


def calculate_range(lst):
    return max(lst) - min(lst)
# Variance

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
# Écart-type (standard deviation)

import math

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
# Exemple d’appel global :

data = [4, 2, 5, 8, 6, 9, 3, 4, 5]

print("\nMoyenne :", calculate_mean(data))
print("\nÉtendue :", calculate_range(data))
print("\nVariance :", calculate_variance(data))
print("\nÉcart-type :", calculate_std(data))

"""

Exercices 3:

"""

#1. Fonction is_prime(n) – Vérifie si un nombre est premier
print("Exercice N°3.1 : Vérification si premier")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print("\n", is_prime(4))
print()

# 2. Vérifier si tous les éléments d'une liste sont uniques
print("Exercice N°3.2 : Vérification des éléments uniques")
def are_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_items_unique([1, 2, 3]))  
print("\n",are_items_unique([1, 2, 2, 3])) 
print()

# 3. Vérifier si tous les éléments ont le même type
print("Exercice N°3.3 : Vérification du même type")
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)


print(all_same_type([1, 2, 3])) 
print("\n",all_same_type([1, "2", 3])) 
print()

# 4. Vérifier si une variable est un identifiant Python valide
print("Exercice N°3.4 : Vérification d'un identifiant valide")
def is_valid_variable(var_name):
    return var_name.isidentifier()

print(is_valid_variable("age"))
print("\n",is_valid_variable("1st_name")) 
print("\n",is_valid_variable("first_name"))
print()

#5. Analyse de données pays – Fichier countries_data.py

countries_data = [
    {'name': 'China', 'population': 1444216107, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1393409038, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 332915073, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 276361783, 'languages': ['Indonesian']},
]

# def most_spoken_languages(n=10):
#     all_languages = []
#     for country in countries_data:
#         all_languages.extend(country['languages'])

#     language_counts = Counter(all_languages)
#     return language_counts.most_common(n)


# print(most_spoken_languages(10))
# Fonction most_populated_countries(n=10)

def most_populated_countries(n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]


for country in most_populated_countries(5):
    print(f"{country['name']} - {country['population']}")