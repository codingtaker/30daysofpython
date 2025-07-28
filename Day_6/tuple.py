# Jour 6 : 30 Days of Python Programming


# 1. Créer un tuple vide
print("Exercice N°1.1 : Tuple vide")
tuple_vide = ()
print("1. Tuple vide :", tuple_vide)
print()

# 2. Créer un tuple avec les noms de tes soeur et freres
print("Exercice N°1.2 : Tuple avec freres et soeurs")
soeur = ('Amina', 'Fatou', 'Salimata')
freres = ('Kossi', 'David')
print("2. soeur :", soeur)
print("   freres :", freres)
print()

# 3. Joindre les deux tuples pour créer un tuple
print("Exercice N°1.3 : Joindre les tuples")
brosist = freres + soeur
print("3. brosist :", brosist)
print()

# 4. Nombre total de freres et soeur
print("Exercice N°1.4 : Nombre total de freres et soeurs")
print("4. Nombre total de freres et soeur :", len(brosist))
print()

# 5. Ajouter les parents au tuple et créer "family_members"
print("Exercice N°1.5 : Ajouter les parents au tuple")
parents = ('Papa', 'Maman')
Family_Members = brosist + parents
print("5. Membres de la famille :", Family_Members)
print()


"""

Exercices 2:

"""

# 1. Déballer les membres de la famille
print("Exercice N°2.1 : Déballer les membres de la famille")
frere1, frere2, soeur1, soeur2, soeur3, père, mère = Family_Members
print("1. freres :", frere1, "et", frere2)
print("   soeurs :", soeur1, soeur2, soeur3)
print("   Père :", père)
print("   Mère :", mère)
print()

# 2. Créer des tuples et les fusionner
print("Exercice N°2.2 : Fusionner des tuples")
fruits = ('orange', 'pomme', 'banane')
legumes = ('carotte', 'tomate', 'chou')
produits_animaux = ('lait', 'oeufs', 'fromage')

food_stuff_tp = fruits + legumes + produits_animaux
print("2. Aliments tuple :", food_stuff_tp)
print()

# 3. Convertir le tuple en liste
print("Exercice N°2.3 : Convertir le tuple en liste")
food_stuff_lt = list(food_stuff_tp)
print("3. Aliments liste :", food_stuff_lt)
print()

# 4. Extraire l'élément du milieu
print("Exercice N°2.4 : Élément du milieu")
n = len(food_stuff_lt)
if n % 2 == 0:
    milieu = food_stuff_lt[n//2 - 1 : n//2 + 1]
else:
    milieu = [food_stuff_lt[n//2]]
print("4. Élément(s) du milieu :", milieu)
print()

# 5. Extraire les 3 premiers et 3 derniers éléments
print("Exercice N°2.5 : Extration des 3 premiers et derniers éléments")
print("5. Trois premiers éléments :", food_stuff_lt[:3])
print("   Trois derniers éléments :", food_stuff_lt[-3:])
print()

# 6. Supprimer complètement le tuple
print("Exercice N°2.5 : Supprimer le tuple")
del food_stuff_tp

# print(food_stuff_tp)   une erreur ve se produire si vous décommentez cette ligne

print("6. Tuple food_stuff_tp supprimé.")
print()

# 7. Vérifier si un élément est dans un tuple
print("Exercice N°2.7 : Vérifier la présence d'un élément")
pays_nordiques = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("7. L'Estonie est-elle un pays nordique ? :", 'Estonia' in pays_nordiques)
print("   L’Islande est-elle un pays nordique ? :", 'Iceland' in pays_nordiques)