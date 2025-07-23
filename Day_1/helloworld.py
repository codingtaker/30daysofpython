# # Day 1 - 30DaysOfPython Challenge
# print(2 + 3) # addition(+)
# print(3 - 1) # subtraction(-)
# print(2 * 3) # multiplication(*)
# print(3 / 2) # division(/)
# print(3 ** 2) # exponential(**)
# print(3 % 2) # modulus(%)
# print(3 // 2) # Floor division operator(//)


# Exercice 1:
# 1. Vérifiez la version Python que vous utilisez:
#python --version

#2. Opérations dans le shell Python
print("Exercice 1-2: Opérations dans le shell Python")
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)
print("")

# 3. Écrivez des chaînes de caractères (strings)
print("Exercice 1-3: Écrire des chaînes de caractères")
print("Nom Benicio")
print("Nom De Famille: ALLAGLO")
print("Pays: Togo")
print("Je profite de 30 jours de python")
print("")


### 4. Vérifiez les types de données
print("Exercice 1-4: Vérification des types de données")
print(type(10)) 
print(type(9.8)) 
print(type(3.14)) 
print(type(4 - 4j))  
print(type(['Asabeneh', 'Python', 'Finlande'])) 
print(type("Votre Nom"))
print(type("Votre Nom De Famille")) 
print(type("Votre Pays"))   
print("")

#Exercice Niveau 3:

# 1. Exemples de différents types de données en Python

# Number
entier = 7  
flottant = 3.14  
complexe = 2 + 3j  

# String
texte = "Bonjour"

# Boolean
est_vrai = True

# List
liste = [1, 2, 3, "Python"]

# Tuple
tuple = (1, "a", 3.5)

# Set
set = {1, 2, 3}

# Dictionary
dict = {"nom": "Seph", "pays": "Togo"}


# 2. Distance euclidienne entre les points (2, 3) et (10, 8) 
# Formule
# sqrt = Racine carré
# distance= \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

import math
print("Exercice 3-2: Distance euclidienne entre les points (2, 3) et (10, 8)")
x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance euclidienne :", distance)

