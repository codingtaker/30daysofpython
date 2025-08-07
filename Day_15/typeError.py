 # Jour 15 : 30 Days of Python Programming

# 1. SyntaxError — Oubli de parenthèses

print 'Bonjour le monde'


# 2. NameError — Variable non définie

print(age)

# 3. IndexError — Accès à un index inexistant dans une liste

nombres = [10, 20, 30]
print(nombres[5])

# 4. ModuleNotFoundError — Mauvais nom de module

import maths

print(math.sqrt(16))  

# 5. AttributeError — Mauvais nom de fonction ou attribut

import math
print(math.PI)


# 6. KeyError — Clé inexistante dans un dictionnaire

user = {'name': 'Alice', 'age': 25}
print(user['email'])


# 7. TypeError — Mauvais type de données

print(5 + '5')


# 8. ImportError — Fonction mal importée

from math import power

print(pow(2, 3)) 

# 9. ValueError — Conversion impossible

int('12a')


# 10. ZeroDivisionError — Division par zéro

print(5 / 0)
