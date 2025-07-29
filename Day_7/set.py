# Jour 7 : 30 Days of Python Programming

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Trouver la longueur de it_companies
print("Exercice N°1.1 : Longueur de it_companies")
print("1. Nombre d'entreprises IT :", len(it_companies))
print()

# 2. Ajouter 'Twitter' à l’ensemble
print("Exercice N°1.2 : Ajouter Twitter")
it_companies.add('Twitter')
print("2. Après ajout de Twitter :", it_companies)
print()

# 3. Ajouter plusieurs entreprises à la fois
print("Exercice N°1.3 : Ajouter plusieurs entreprises")
it_companies.update(['Tesla', 'Airbnb', 'Spotify'])
print("3. Après ajout multiple :", it_companies)
print()

# 4. Supprimer une entreprise
print("Exercice N°1.4 : Supprimer une entreprise")
it_companies.remove('IBM')  # Supprime 'IBM'
print("4. Après suppression de IBM :", it_companies)
print()

# 5. Différence entre remove() et discard()
print("Exercice N°1.5 : Différence entre remove() et discard")
print("5. Différence entre remove et discard :")
print("- remove() génère une erreur si l’élément n’existe pas.")
print("- discard() ne génère pas d’erreur si l’élément n’est pas présent.")
# Exemple:
it_companies.discard('Inexistant')

try:
    it_companies.remove('Inexistant')
except KeyError:
    print("  -> remove a déclenché une erreur car l'élément n'existe pas.")


"""

Exercices 2:

"""

#1. Union de A et B
print("Exercice N°2.1 : Union de A et B")
union_AB = A.union(B)
print("1. Union de A et B :", union_AB)
print()

#2. Intersection de A et B
print("Exercice N°2.2 : Intersection de A et B")
intersection_AB = A.intersection(B)
print("2. Intersection de A et B :", intersection_AB)
print()

#3. Est-ce que A est un sous-ensemble de B ?
print("Exercice N°2.3 : Sous-ensemble de A dans B")
is_subset = A.issubset(B)
print("3. A est un sous-ensemble de B :", is_subset)
print()

#4. A et B sont-ils disjoints ?
print("Exercice N°2.4 : A et B disjoints")
is_disjoint = A.isdisjoint(B)
print("4. A et B sont disjoints :", is_disjoint)
print()

#5. Union A avec B, puis B avec A (équivalent)
print("Exercice N°2.5 : Union A et B, puis B et A")
union_A_B = A.union(B)
union_B_A = B.union(A)
print("5. A U B :", union_A_B)
print("   B U A :", union_B_A)

#6. Différence symétrique entre A et B
print("Exercice N°2.6 : Différence symétrique entre A et B")
sym_diff = A.symmetric_difference(B)
print("6. Différence symétrique (éléments non communs) :", sym_diff)
print()

#7. Supprimer totalement les ensembles
print("Exercice N°2.7 : Supprimer les ensembles A et B")
del A
del B
print("7. Les ensembles A et B ont été supprimés.")
print()

"""

Exercices 3:

"""

# Conversion en set
ages_set = set(ages)
print("Exercice N°3.1 : Conversion de la liste d'âges en set")
print("1. Longueur de la liste d'âges :", len(ages))
print("   Longueur du set d'âges :", len(ages_set))

if len(ages) > len(ages_set):
    print("La liste contient plus d'éléments (car elle autorise les doublons).")
else:
    print("Le set contient autant ou plus d'éléments (très improbable sans doublons).")
print()

#2. Différences entre string, list, tuple, set
"""
- String:
  - Chaîne de caractères (texte)
  - Immutable (ne peut pas être modifiée directement)
  - Indexable et itérable
  - Ex : "Bonjour le monde"

- List :
  - Collection ordonnée et mutable
  - Accepte les doublons
  - Définie avec des crochets : `[]`
  - Ex : [1, 2, 3]

- Tuple :
  - Collection ordonnée et immutable
  - Accepte les doublons
  - Définie avec des parenthèses : `()`
  - Ex : (1, 2, 3)

- Set (ensemble) :
  - Collection non ordonnée, non indexable, sans doublons
  - Mutable (on peut y ajouter/retirer des éléments)
  - Définie avec des accolades : `{}` ou `set()`
  - Ex : {1, 2, 3}

"""
#3. Compter les mots uniques dans une phrase

phrase = "I am a teacher and I love to inspire and teach people"

# 1. Découper en mots
mots = phrase.split()

# 2. Convertir en set pour ne garder que les mots uniques
mots_uniques = set(mots)

print("3. Nombre de mots uniques :", len(mots_uniques))
print("   Mots uniques :", mots_uniques)