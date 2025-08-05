 # Jour 14 : 30 Days of Python Programming

"""

Exercices 1:


1. Différence entre map, filter et reduce :
map transforme chaque élément d’une liste avec une fonction.
filter sélectionne les éléments selon une condition.
reduce combine tous les éléments en une seule valeur (ex. somme).

2. Différence entre higher-order function, closure et decorator :
Higher-order function : prend ou retourne une fonction.
Closure : fonction interne qui retient les variables de l’extérieur.
Decorator : fonction qui modifie le comportement d’une autre via @.

"""

# 3. Définir une fonction et l’utiliser avec map, filter, reduce

def square(n):
    return n * n

from functools import reduce

numbers = [1, 2, 3, 4]

# map
squares = list(map(square, numbers))  # ➜ [1, 4, 9, 16]

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))  # ➜ [2, 4]

# reduce
total = reduce(lambda x, y: x + y, numbers)  # ➜ 10

print("Squares:", squares)
print("Evens:", evens)
print("Total:", total)
# 4. Afficher chaque pays avec une boucle for

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for country in countries:
    print(country)
# 5. Afficher chaque nom avec for

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

for name in names:
    print(name)
# 6. Afficher chaque nombre avec for

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number, end=' ')

print()


"""

Exercices 2:

"""


# 1. Utiliser map pour mettre les noms des pays en majuscules

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
upper_countries = list(map(str.upper, countries))
print(upper_countries)

# 2. Utiliser map pour élever les nombres au carré

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# 3. Utiliser map pour mettre les noms en majuscules

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_names = list(map(str.upper, names))
print(upper_names)

# 4. Utiliser filter pour garder les pays contenant "land"

land_countries = list(filter(lambda country: 'land' in country, countries))
print(land_countries)

# 5. Utiliser filter pour garder les pays de 6 lettres exactement

six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print(six_char_countries)

# 6. Utiliser filter pour garder les pays avec 6 lettres ou plus

six_or_more = list(filter(lambda c: len(c) >= 6, countries))
print(six_or_more)

# 7. Utiliser filter pour garder les pays qui commencent par "E"

start_with_E = list(filter(lambda c: c.startswith('E'), countries))
print(start_with_E)

# 8. Chaîner plusieurs itérateurs (map, filter, reduce)

from functools import reduce

result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x ** 2, numbers)
    )
)
print("Somme des carrés pairs :", result)

# 9. Fonction get_string_lists pour ne garder que les chaînes

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print(get_string_lists(['hello', 123, True, 'world', 3.14]))  # ➜ ['hello', 'world']

# 10. Utiliser reduce pour faire la somme des nombres

total = reduce(lambda x, y: x + y, numbers)
print("Somme :", total)

# 11. Utiliser reduce pour concaténer les pays dans une phrase

sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + f", and {countries[-1]} are north European countries."
print(sentence)

# 12. Fonction categorize_countries

def categorize_countries(pattern):
    return [country for country in countries if pattern in country]

print(categorize_countries('land'))  # ['Finland', 'Iceland']

# 13. Dictionnaire des pays par initiales

def country_dict_by_initial(countries):
    from collections import defaultdict
    d = defaultdict(int)
    for country in countries:
        d[country[0]] += 1
    return dict(d)

print(country_dict_by_initial(countries))

# 14. Fonction pour les 10 premiers pays

def get_first_ten_countries(countries):
    return countries[:10]

# Exemple avec une liste fictive plus longue :
long_list = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Germany', 'France', 'Spain', 'Italy', 'Portugal']
print(get_first_ten_countries(long_list))

# 15. Fonction pour les 10 derniers pays

def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(long_list))
print()

