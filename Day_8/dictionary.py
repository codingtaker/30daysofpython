# Jour 8 : 30 Days of Python Programming

#1. Créer un dictionnaire vide appelé chien
print("Exercice N°1 : Dictionnaire vide")
chien = {}
print("1. Dictionnaire vide :", chien)
print()

#2. Ajouter des clés : nom, couleur, race, pattes, âge
print("Exercice N°2 : Ajouter des clés au dictionnaire chien")
chien['nom'] = 'Rex'
chien['couleur'] = 'marron'
chien['race'] = 'Berger Allemand'
chien['pattes'] = 4
chien['âge'] = 5
print("2. Dictionnaire du chien :", chien)
print()

#3. Créer un dictionnaire étudiant avec plusieurs clés
print("Exercice N°3 : Dictionnaire étudiant")
student = {
    'prenom': 'Ali',
    'nom': 'Traoré',
    'genre': 'Masculin',
    'âge': 22,
    'marié': False,
    'compétences': ['Python', 'Reactjs'],
    'pays': 'Ghana',
    'ville': 'Accra',
    'adresse': 'Rue 22 st Joseph'
}
print("3. Dictionnaire étudiant :", student)
print()

#4. Obtenir la longueur du dictionnaire student
print("Exercice N°4 : Longueur du dictionnaire student")
print("4. Nombre d’éléments dans le dictionnaire student :", len(student))
print() 

#5. Obtenir la valeur de compétences et vérifier le type
print("Exercice N°5 : Valeur de compétences")
print("5. Compétences :", student['compétences'])
print("   Type de 'compétences' :", type(student['compétences']))
print()

#6. Ajouter une ou deux compétences
print("Exercice N°6 : Ajouter des compétences")
student['compétences'].append('Django')
student['compétences'].append('JavaScript')
print("6. Compétences après ajout :", student['compétences'])
print()

#7. Obtenir les clés sous forme de liste
print("Exercice N°7 : Clés du dictionnaire")
cles = list(student.keys())
print("7. Clés du dictionnaire :", cles)
print()

#8. Obtenir les valeurs sous forme de liste
print("Exercice N°8 : Valeurs du dictionnaire")
valeurs = list(student.values())
print("8. Valeurs du dictionnaire :", valeurs)
print()

#9. Convertir en liste de tuples avec items()
print("Exercice N°9 : Convertir en liste de tuples")
tuples = list(student.items())
print("9. Liste de tuples :", tuples)
print()

#10. Supprimer un élément du dictionnaire
print("Exercice N°10 : Supprimer un élément")
del student['adresse']
print("10. addresse supprimé :", student)
print()
#11. Supprimer tout le dictionnaire chien
print("Exercice N°11 : Supprimer le dictionnaire chien")
del chien
print("11. Le dictionnaire 'chien' a été supprimé.")