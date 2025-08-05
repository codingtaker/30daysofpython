 # Jour 12 : 30 Days of Python Programming

"""

Exercices 1:

"""
import random
import string

#1. Fonction random_user_id() 
print("Exercice 1.1: Fonction random")
def random_user_id():
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(characters, k=6))
print(random_user_id()) 
print()

# 2. Fonction user_id_gen_by_user()
print("Exercice 1.2: Fonction user_id_gen_by_user")
def user_id_gen_by_user():
    num_chars = int(input("Nombre de caractères par ID : "))
    num_ids = int(input("Nombre d'IDs à générer : "))

    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        print(user_id)
print()

# 3. Fonction rgb_color_gen()
print("Exercice 1.3: Fonction rgb_color_gen")
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())  # Ex: rgb(125,244,255)
print()

"""

Exercices 2:

"""

#1. Fonction list_of_hexa_colors(n)
print("Exercice 2.1: Fonction list")
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        colors.append(hex_color)
    return colors
print(list_of_hexa_colors(3))
print()

# 2. Fonction list_of_rgb_colors(n)
print("Exercice 2.2: Fonction list de rgb_colors")
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")
    return colors
print(list_of_rgb_colors(2))
print()

# 3. Fonction generate_colors(type, n) 
print("Exercice 2.3: Fonction generate_colors")
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type de couleur invalide. Utilisez 'hexa' ou 'rgb'."

print(generate_colors('hexa', 3)) 
print(generate_colors('\nrgb', 2))
print()

"""

Exercices 3:

"""
#1. Fonction shuffle_list(lst)
print("Exercice 3.1: Fonction shuffle_list")
def shuffle_list(lst):
    shuffled = lst[:]     
    random.shuffle(shuffled) 
    return shuffled
ma_liste = [1, 2, 3, 4, 5, 6, 7]
print("Liste mélangée :", shuffle_list(ma_liste))
print()

# 2. Fonction generate_unique_random() 
print("Exercice 3.2: Fonction generate_unique_random")
def generate_unique_random():
    return random.sample(range(10), 7)

print("Nombres aléatoires uniques :", generate_unique_random())  