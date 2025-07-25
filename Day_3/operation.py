# Jour 3 : 30 Days of Python Programming

import math

# 1. Âge entier
age = 25

# 2. Taille (float)
taille = 1.75  # en mètres

# 3. Nombre complexe
nombre_complexe = 3 + 4j

# 4. Aire d’un triangle à partir de la base et hauteur
print("Exercice N°4 : Aire d’un triangle")
base = float(input("Entrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))
aire_triangle = 0.5 * base * hauteur
print("La zone du triangle est :", aire_triangle)
print("")

# 5. Périmètre d’un triangle
print("Exercice N°5 : Périmètre d’un triangle")
a = float(input("Entrez le côté A du triangle : "))
b = float(input("Entrez le côté B du triangle : "))
c = float(input("Entrez le côté C du triangle : "))
perimetre_triangle = a + b + c
print("Le périmètre du triangle est :", perimetre_triangle)
print("")

# 6. Aire et périmètre d’un rectangle
print("Exercice N°6 : Aire et périmètre d’un rectangle")
longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
aire_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("Aire du rectangle :", aire_rectangle)
print("Périmètre du rectangle :", perimetre_rectangle)
print("")

# 7. Aire et circonférence d’un cercle
print("Exercice N°7 : Aire et circonférence d’un cercle")
rayon = float(input("Entrez le rayon du cercle : "))
pi = 3.14
aire_cercle = pi * rayon ** 2
circonference = 2 * pi * rayon
print("Aire du cercle :", aire_cercle)
print("Circonférence du cercle :", circonference)
print("")

# 8. Equation
print("Exercice N°8 : Equation")
x = 0
y = 2 * x - 2
print("Quand x = 0, y =", y)


y = 0
x_ordonnee = (y + 2) / 2
print("Quand y = 0, x =", x_ordonnee)

pente_eq = 2  
print("La pente de y = 2x - 2 est :", pente_eq)
print("")

# 9. Pente et distance entre (2, 2) et (6, 10)
print("Exercice N°9 : Pente et distance entre deux points")
x1, y1 = 2, 2
x2, y2 = 6, 10

pente_points = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Pente entre les points :", pente_points)
print("Distance euclidienne :", distance)
print("")

# 10. Comparaison des pentes
print("Exercice N°10 : Comparaison des pentes")
print("La pente de l'équation (2) est-elle égale à celle entre les points ?", pente_eq == pente_points)
print("")

# 11. Résolution y
print("Exercice N°11 : Résolution de l'équation ")
x_values = [-5, -4, -3, -2, -1, 0]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"Pour x = {x}, y = {y}")
print("")

# 12. Comparaison de longueur de 'Python' et 'Dragon'
print("Exercice N°12 : Comparaison de longueur")
long_python = len("Python")
long_dragon = len("Dragon")
print("Longueur 'Python' :", long_python)
print("Longueur 'Dragon' :", long_dragon)
print("Comparaison Falsy :", long_python == long_dragon)
print("")

#13. Vérifier si "on" est dans les deux mots
print("Exercice N°13 : Vérification de sous-chaîne")
print("on" in "python" and "on" in "dragon") 
print("")

#14. Vérifier si "jargon" est dans la phrase
print("Exercice N°14 ")
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
print("")

# 15. Il n’y a pas de 'on' dans les deux ?
print("Exercice N°15 : Vérification de 'on' dans les mots")
print("on" not in "dragon" and "on" not in "python")
print("")

# 16. Longueur de "python" → float → str
print("Exercice N°16 : Conversion de type")
length_python = len("python")  
length_float = float(length_python) 
length_str = str(length_float)  
print(length_str)
print("")

# 17. Vérifier si un nombre est pair
print("Exercice N°17 : Vérification de nombre pair")
num = int(input("Entrez un nombre : "))
if num % 2 == 0:
    print("Nombre pair")
else:
    print("Nombre impair")
print("")  

#18. Division entière 7 // 3 == int(2.7) ?
print("Exercice N°18 : Division entière")
print(7 // 3 == int(2.7)) 
print("")

# 19. type('10') == type(10) ?
print("Exercice N°19 : Comparaison de type")
print(type('10') == type(10))
print("")

# 20. int('9.8') == 10 ?
print("Exercice N°20 : Conversion de type")
# Cela déclenchera une erreur car '9.8' ne peut pas être converti directement en int
try:
    print(int('9.8') == 10)
except ValueError:
    print("Erreur : '9.8' ne peut pas être converti directement en entier.")
print("")

#21. Script pour calculer le salaire hebdomadaire
print("Exercice N°21 : Calcul du salaire hebdomadaire")
heures = float(input("Entrez le nombre d'heures : "))
taux = float(input("Entrez le taux par heure : "))
gain = heures * taux
print("Votre gain hebdomadaire est", gain)
print("")

#22. Script pour calculer les secondes vécues
print("Exercice N°22 : Calcul des secondes vécues")
annees_vécues = int(input("Entrez le nombre d'années que vous avez vécues : "))
secondes_par_annee = 365 * 24 * 60 * 60
total_secondes = annees_vécues * secondes_par_annee
print(f"Vous avez vécu pendant {total_secondes} secondes.")
print("")
# 23. Affichage de la table formatée
print("Exercice N°23 : Affichage de la table formatée")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")