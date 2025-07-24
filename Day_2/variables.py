# Jour 2: 30 Days of Python Programming

# Exercice niveau 1
print("Exercice Niveau 1")
print("")
# 3. Prénom
prenom = "Seph"
print("Prénom:", prenom)

# 4. Nom de famille
nom_de_famille = "Kanzaki"
print("Nom de famille:", nom_de_famille)

# 5. Nom complet
nom_complet = prenom + " " + nom_de_famille
print("Nom complet:", nom_complet)

# 6. Pays
pays = "Togo"
print("Pays:", pays)

# 7. Municipalité (ville)
municipalite = "Lomé"
print("Municipalité:", municipalite)

# 8. Âge
age = 25
print("Âge:", age)

# 9. Marié ou non
est_marie = False
print("Marié:", est_marie)

# 10. Variable is_true
is_true = True
print("is_true:", is_true)

# 11. Lumière allumée ou non
is_light_on = True
print("Lumière allumée:", is_light_on)

# 12. Plusieurs variables déclarées sur une seule ligne
FirstName, Age, Origine = "Kanza", 22, "Togo"
print(f"Je me nomme {FirstName}, j'ai {Age} ans et je suis originaire de {Origine}.")
print("")   

#Exercice Niveau 2
print("Exercice Niveau 2")
print("")
# 1. Vérification des types de données
print("Type de prenom :", type(prenom))
print("Type de nom_de_famille :", type(nom_de_famille))
print("Type de nom_complet :", type(nom_complet))
print("Type de pays :", type(pays))
print("Type de municipalite :", type(municipalite))
print("Type de age :", type(age))
print("Type de est_marie :", type(est_marie))
print("Type de is_true :", type(is_true))
print("Type de is_light_on :", type(is_light_on))
print("")

# 2. Longueur du prénom
print("Longueur du prénom :", len(prenom))
print("")

# 3. Comparaison de la longueur du prénom et du nom de famille avec une condition
taille_prenom = len(prenom)
taille_nom_famille = len(nom_de_famille)

if taille_prenom > taille_nom_famille:
    print("Le prénom est plus long que le nom de famille.")
elif taille_prenom == taille_nom_famille:
    print("Le prénom et le nom de famille ont la même longueur.")
else:
    print("Le nom de famille est plus long que le prénom.")
print("")

# 4. Déclaration des nombres
num_one = 5
num_two = 4
print("")

# 5. Addition
somme = num_one + num_two
print("Addition :", somme)
print("")

# 6. Soustraction
difference = num_one - num_two
print("Soustraction :", difference)
print("")

# 7. Multiplication
produit = num_one * num_two
print("Multiplication :", produit)
print("")

# 8. Division
division = num_one / num_two
print("Division :", division)
print("")

# 9. Modulo 
reste = num_one % num_two
print("Le reste de la division :", reste)
print("")

# 10. Floor Division 
floor_division = num_one // num_two
print("Division entière (floor) :", floor_division)
print("")

# 12. Calculs avec un cercle
import math

rayon = 30
area_of_circle = math.pi * rayon ** 2
print("Aire du cercle :", area_of_circle)

circum_of_circle = 2 * math.pi * rayon
print("Circonférence du cercle :", circum_of_circle)

rayon_utilisateur = float(input("Entrez le rayon du cercle : "))
aire_user = math.pi * rayon_utilisateur ** 2
print("Aire du cercle :", aire_user)
print("")

# 13. Entrées utilisateur
prenom_user = input("Entrez votre prénom : ")
nom_user = input("Entrez votre nom de famille : ")
pays_user = input("Entrez votre pays : ")
age_user = input("Entrez votre âge : ")

print(f"Je me nomme {prenom_user} {nom_user}, j'ai {age_user} ans et je suis originaire de {pays_user}.")

print("")

# 14. Liste des mots-clés réservés en Python
help("keywords")
