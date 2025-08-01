# Jour 9 : 30 Days of Python Programming


"""

Exercices 1:

"""

#1. Vérifier l'âge de conduite
print("Exercice N°1.1 : Vérification de l'âge de conduite")
âge = int(input("1. Entrez votre âge : "))

if âge >= 18:
    print("Vous avez l'âge requis pour apprendre à conduire.")
else:
    années_restantes = 18 - âge
    if années_restantes == 1:
        print("Vous devez attendre encore 1 an pour apprendre à conduire.")
    else:
        print(f"Vous devez attendre encore {années_restantes} ans pour apprendre à conduire.")
print()

#2. Comparaison d’âge
print("Exercice N°1.2 : Comparaison d'âge")
my_age = 25
your_age = int(input("\n2. Entrez votre âge : "))

diff = abs(my_age - your_age)

if your_age > my_age:
    print(f"Vous avez {diff} {'an' if diff == 1 else 'ans'} de plus que moi.")
elif your_age < my_age:
    print(f"J’ai {diff} {'an' if diff == 1 else 'ans'} de plus que vous.")
else:
    print("Nous avons le même âge.")

print()

#3. Comparer deux nombres entrés par l'utilisateur
print("Exercice N°1.3 : Comparaison de deux nombres")
a = float(input("\n3. Entrez le premier nombre : "))
b = float(input("   Entrez le deuxième nombre : "))

if a > b:
    print(f"{a} est supérieur à {b}.")
elif a < b:
    print(f"{a} est inférieur à {b}.")
else:
    print(f"{a} est égal à {b}.")
print()

"""

Exercices 2:

"""

#1. Attribuer une note selon le score
print("Exercice N°2.1 : Attribution de note")
score = int(input("1. Entrez votre score (0 à 100) : "))

if 80 <= score <= 100:
    print("Note : A")
elif 70 <= score < 80:
    print("Note : B")
elif 60 <= score < 70:
    print("Note : C")
elif 50 <= score < 60:
    print("Note : D")
elif 0 <= score < 50:
    print("Note : F")
else:
    print("Score invalide. Veuillez entrer un nombre entre 0 et 100.")

print()

#2. Déterminer la saison selon le mois
print("Exercice N°2.2 : Détermination de la saison")
mois = input("\n2. Entrez le nom d’un mois : ").capitalize()

if mois in ['Septembre', 'Octobre', 'Novembre']:
    print("Saison : Automne")
elif mois in ['Décembre', 'Janvier', 'Février']:
    print("Saison : Hiver")
elif mois in ['Mars', 'Avril', 'Mai']:
    print("Saison : Printemps ")
elif mois in ['Juin', 'Juillet', 'Août']:
    print("Saison : Été")
else:
    print("Mois non reconnu.")

print()

#3. Ajouter un fruit s’il n’existe pas dans la liste
print("Exercice N°2.3 : Ajouter un fruit")
fruits = ['banana', 'orange', 'mango', 'lemon']
nouveau_fruit = input("\n3. Entrez un fruit : ").lower()

if nouveau_fruit in fruits:
    print("Ce fruit est déjà dans la liste.")
else:
    fruits.append(nouveau_fruit)
    print("Fruit ajouté ! Nouvelle liste :", fruits)
print()


"""

Exercices 3:

"""

# Données de départ :
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#1. Vérifier si skills existe et afficher la compétence du milieu
print("Exercice N°3.1 : Compétence du milieu")
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("1. Compétence du milieu :", skills[middle_index])
print()

#2. Vérifier si Python est dans les compétences
print("Exercice N°3.2 : Vérification de Python")
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("2. La personne connaît Python :", has_python)
print()

#3. Déterminer le rôle du développeur
print("Exercice N°3.3 : Rôle du développeur")
if 'skills' in person:
    s = set(person['skills'])

    if s == {'JavaScript', 'React'}:
        print("3. Il est développeur Front-End.")
    elif {'Node', 'Python', 'MongoDB'}.issubset(s):
        print("3. Il est développeur Back-End.")
    elif {'React', 'Node', 'MongoDB'}.issubset(s):
        print("3. Il est développeur Fullstack.")
    else:
        print("3. Titre de développeur inconnu.")

print()

#4. Vérifier s’il est marié et s’il vit en Finlande
print("Exercice N°3.4 : Vérification de l'état civil et du pays")
if person.get('is_marred') and person.get('country') == 'Finland':
    prenom = person['first_name']
    nom = person['last_name']
    pays = person['country']
    print(f"4. {prenom} {nom} vit en {pays}. Il est marié.")