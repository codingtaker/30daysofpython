# Jour 5 : 30 Days of Python Programming

# 1. Déclaration d'une liste vide
print("Exercice N°1.1 : Liste vide")
liste_vide = []
print("")

# 2. Déclaration d'une liste avec plus de 5 éléments
print("Exercice N°1.2 : Liste avec plus de 5 éléments")
ma_liste = ["poulet", "pomme", "attièket", "ananas", "poulet", "Ayimolou"]
print("")

# 3. Longueur de la liste
print("Exercice N°1.3 : Longueur de la liste")
print("3. Longueur de la liste :", len(ma_liste))
print("")

# 4. Premier, milieu et dernier élément
print("Exercice N°1.4 : Premier, milieu et dernier élément")
milieu = ma_liste[len(ma_liste) // 2]
print("4. Premier élément :", ma_liste[0])
print("   Élément du milieu :", milieu)
print("   Dernier élément :", ma_liste[-1])
print("")

# 5. Liste mixte avec types de données différents
print("Exercice N°1.5 : Liste mixte")
mixed_data_types = ["Dum koffi", 25, 1.95, "Célibataire", "Lomé"]
print("5. Données personnelles :", mixed_data_types)
print("")

# 6. Liste des entreprises IT
print("Exercice N°1.6 : Liste des entreprises IT")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("")

# 7. Affichage de la liste
print("Exercice N°1.7 : Affichage de la liste")
print("7. Liste complète :", it_companies)
print("")

# 8. Nombre d'entreprises
print("Exercice N°1.8 : Nombre d'entreprises")
print("8. Nombre d'entreprises :", len(it_companies))
print("")

# 9. Premier, milieu et dernier élément
print("Exercice N°1.9 : Premier, milieu et dernier élément")
milieu_it = it_companies[len(it_companies) // 2]
print("9. Première entreprise :", it_companies[0])
print("   Entreprise du milieu :", milieu_it)
print("   Dernière entreprise :", it_companies[-1])
print("")

# 10. Modification d'une entreprise
print("Exercice N°1.10 : Modification d'une entreprise")
it_companies[1] = "Meta"
print("10. Après modification :", it_companies)
print("")

# 11. Ajout d'une entreprise
print("Exercice N°1.11 : Ajout d'une entreprise")
it_companies.append("Twitter")
print("11. Après ajout :", it_companies)
print("")

# 12. Insertion au milieu
print("Exercice N°1.12 : Insertion au milieu")
it_companies.insert(len(it_companies) // 2, "Tesla")
print("12. Après insertion au milieu :", it_companies)
print("")

# 13. Passage d’un nom en majuscule (sauf IBM)
print("Exercice N°1.13 : Passage d’un nom en majuscule")
it_companies[0] = it_companies[0].upper()
print("13. Après mise en majuscule :", it_companies)
print("")

# 14. Jointure avec '#; '
print("Exercice N°1.14 : Jointure avec '#; '")
jointure = "#; ".join(it_companies)
print("14. Liste jointe :", jointure)
print("")

# 15. Vérifier si une entreprise existe
print("Exercice N°1.15 : Vérifier si une entreprise existe")
print("15. 'Google' est-elle dans la liste ? :", "Google" in it_companies)
print("")

# 16. Tri de la liste
print("Exercice N°1.16 : Tri de la liste")
it_companies.sort()
print("16. Liste triée :", it_companies)
print("")

# 17. Inversion (ordre décroissant)
print("Exercice N°1.17 : Inversion de la liste")
it_companies.reverse()
print("17. Liste inversée :", it_companies)
print("")

# 18. Extraire les 3 premières entreprises
print("Exercice N°1.18 : Extraire les 3 premières entreprises")
print("18. Trois premières entreprises :", it_companies[:3])
print("")

# 19. Extraire les 3 dernières entreprises
print("Exercice N°1.19 : Extraire les 3 dernières entreprises")
print("19. Trois dernières entreprises :", it_companies[-3:])
print("")

# 20. Extraire l'entreprise du milieu
print("Exercice N°1.20 : Extraire l'entreprise du milieu")
milieu_index = len(it_companies) // 2
if len(it_companies) % 2 == 1:
    print("20. Entreprise du milieu :", it_companies[milieu_index])
else:
    print("20. Entreprises du milieu :", it_companies[milieu_index - 1:milieu_index + 1])
print("")

# 21. Supprimer la première entreprise
print("Exercice N°1.21 : Supprimer la première entreprise")
it_companies.pop(0)
print("21. Après suppression du premier élément :", it_companies)
print("")

# 22. Supprimer celle du milieu
print("Exercice N°1.22 : Supprimer celle du milieu")
milieu_index = len(it_companies) // 2
it_companies.pop(milieu_index)
print("22. Après suppression du milieu :", it_companies)
print("")

# 23. Supprimer la dernière entreprise
print("Exercice N°1.23 : Supprimer la dernière entreprise")
it_companies.pop()
print("23. Après suppression du dernier élément :", it_companies)
print("")

# 24. Supprimer toutes les entreprises
print("Exercice N°1.24 : Supprimer toutes les entreprises")
it_companies.clear()
print("24. Liste vidée :", it_companies)
print("")

# 25. Détruire complètement la liste
print("Exercice N°1.25 : Détruire complètement la liste")
del it_companies
print("25. Liste supprimée.")
print("")

# 26. Fusionner front_end et back_end
print("Exercice N°1.26 : Fusionner front_end et back_end")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("26. Stack fusionné :", full_stack)
print("")

# 27. Insertion de Python et SQL après Redux
print("Exercice N°1.27 : Insertion de Python et SQL après Redux")
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("27. Stack complet :", full_stack)
print("")



"""

Exercices 2:

"""

# 1. Analyse d'une liste d’âges
print("Exercice N°2.1 : Analyse d'une liste d’âges")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier la liste
ages.sort()
print("1. Liste triée :", ages)

# Trouver l'âge min et max
min_age = min(ages)
max_age = max(ages)
print("2. Âge minimum :", min_age)
print("   Âge maximum :", max_age)

# Ajouter min et max à la liste
ages.extend([min_age, max_age])
print("3. Après ajout de min et max :", ages)

# Trouver la médiane
ages.sort()
n = len(ages)
if n % 2 == 0:
    mediane = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    mediane = ages[n//2]
print("4. Médiane :", mediane)

# Moyenne
moyenne = sum(ages) / len(ages)
print("5. Moyenne :", moyenne)

# Étendue (range)
etendue = max_age - min_age
print("6. Étendue :", etendue)

# Comparaison des distances au centre
diff_min = abs(min_age - moyenne)
diff_max = abs(max_age - moyenne)
print("7. min - moyenne =", diff_min)
print("   max - moyenne =", diff_max)


# 2. Trouver le/les pays du milieu
print("\nExercice N°2.2 : pays du milieu\n")
pays = ['Bénin', 'Togo', 'Ghana', 'Côte d’Ivoire', 'Niger', 'Mali', 'Burkina Faso']
n = len(pays)

if n % 2 == 1:
    print("Milieu :", pays[n//2])
else:
    print("Milieu :", pays[n//2 - 1], "et", pays[n//2])


# 3. Diviser la liste de pays en deux moitiés
print("\nExercice N°2.3 : Diviser la liste de pays \n")
moitie = (n + 1) // 2 
premiere_moitie = pays[:moitie]
deuxieme_moitie = pays[moitie:]
print("Première moitié :", premiere_moitie)
print("Deuxième moitié :", deuxieme_moitie)


# 4. Unpacking des pays
print("\nExercice N°2.4 : Unpacking des pays\n")
liste_pays = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

pays1, pays2, pays3, *pays_scandinaves = liste_pays

print("Pays 1 :", pays1)
print("Pays 2 :", pays2)
print("Pays 3 :", pays3)
print("Pays scandinaves :", pays_scandinaves)