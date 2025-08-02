# Jour 10 : 30 Days of Python Programming


"""

Exercices 1:

"""

#1. Itérer de 0 à 10 avec for et while
print("Exercice N°1.1 : Itération de 0 à 10")
print("1. Boucle for de 0 à 10 :")
for i in range(11):
    print(i)
print("\n1. Boucle while de 0 à 10 :")
print()
i = 0
while i <= 10:
    print(i)
    i += 1

#2. Itérer de 10 à 0 avec for et while
print("\nExercice N°1.2 : Itération de 10 à 0")
print("2. Boucle for de 10 à 0 :")
for i in range(10, -1, -1):
    print(i)
print("\n2. Boucle while de 10 à 0 :")
i = 10
while i >= 0:
    print(i)
    i -= 1

#3. Triangle en # (7 lignes)
print("\nExercice N°1.3 : Triangle en #")
print("3. Triangle :")
for i in range(1, 8):
    print("#" * i)

#4. Carré 8 x 8 avec boucle imbriquée
print("\nExercice N°1.4 : Carré 8x8")
print("4. Carré 8x8 :")
for i in range(8):
    for j in range(8):
        print("#", end="")
    print()

#5. Affichage des produits x * x de 0 à 10
print("\nExercice N°1.5 : Table des carrés")
print("5. Table des carrés :")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#6. Itération d'une liste
print("\nExercice N°1.6 : Itération de la liste")
print("6. Itération de la liste :")
technos = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in technos:
    print(tech)

#7. Afficher les nombres pairs de 0 à 100
print("\nExercice N°1.7 : Nombres pairs de 0 à 100")
print("7. Nombres pairs de 0 à 100 :")
for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print()

#8. Afficher les nombres impairs de 0 à 100
print("\nExercice N°1.8 : Nombres impairs de 0 à 100")
print("8. Nombres impairs de 0 à 100 :")
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print()

"""

Exercices 2:

"""


#1. Somme de tous les nombres de 0 à 100
print("\nExercice N°2.1 : Somme de 0 à 100")
somme_totale = 0

for i in range(101):
    somme_totale += i

print(f"1. La somme de tous les nombres de 0 à 100 est : {somme_totale}")


# 2. Somme des nombres pairs et impairs de 0 à 100
print("\nExercice N°2.2 : Somme des nombres pairs et impairs de 0 à 100")   
somme_pairs = 0
somme_impairs = 0

for i in range(101):
    if i % 2 == 0:
        somme_pairs += i
    else:
        somme_impairs += i

print(f"\n2. La somme des nombres pairs est : {somme_pairs}")
print(f"   La somme des nombres impairs est : {somme_impairs}")


"""

Exercices 3:

"""

#1. Parcourir les pays contenant "land"
print("\nExercice N°3.1 : Pays contenant 'land'")
countries = ['Finland', 'Sweden', 'Iceland', 'Estonia', 'Thailand', 'Germany', 'Ireland', 'Canada']

# from countries import countries
pays_land = []

for pays in countries:
    if 'land' in pays:
        pays_land.append(pays)

print("1. Pays contenant 'land' :", pays_land)

# 2. Inverser une liste de fruits avec une boucle
print("\nExercice N°3.2 : Inverser une liste de fruits")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_inversés = []

for i in range(len(fruits) - 1, -1, -1):
    fruits_inversés.append(fruits[i])

print("2. Fruits dans l’ordre inversé :", fruits_inversés)


# 3. Analyse des données dans countries_data.py
print("\nExercice N°3.3 : Analyse des données des pays")
countries_data = [
    {'name': 'China', 'population': 1439323776, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1380004385, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331002651, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523615, 'languages': ['Indonesian']},
    {'name': 'Brazil', 'population': 212559417, 'languages': ['Portuguese']},
    {'name': 'Pakistan', 'population': 220892340, 'languages': ['Urdu', 'English']}
]
# i. Nombre total de langues uniques

# from countries_data import countries_data
langues_uniques = set()

for pays in countries_data:
    for langue in pays['languages']:
        langues_uniques.add(langue)

print("3.i. Nombre total de langues :", len(langues_uniques))
# ii. Les 10 langues les plus parlées

from collections import Counter

compteur_langues = Counter()

for pays in countries_data:
    for langue in pays['languages']:
        compteur_langues[langue] += 1

langues_populaires = compteur_langues.most_common(10)

print("3.ii. Les 10 langues les plus parlées :")
for langue, nombre in langues_populaires:
    print(f" - {langue}: {nombre} pays")
# iii. Les 10 pays les plus peuplés

pays_trié_par_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("3.iii. Les 10 pays les plus peuplés :")
for pays in pays_trié_par_population[:10]:
    print(f" - {pays['name']}: {pays['population']}")