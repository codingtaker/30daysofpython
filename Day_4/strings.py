# Jour 4 : 30 Days of Python Programming

# 1. Concaténation
print("Exercice N°1 : Concaténation de chaînes")
chaine1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print("1. Chaîne concaténée :", chaine1)
print()

# 2. Autre concaténation
print("Exercice N°2 : Autre concaténation")
chaine2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print("2. Chaîne concaténée :", chaine2)
print()

# 3. Déclaration d'une variable
print("Exercice N°3 : Déclaration d'une variable")
company = "Coding For All"
print("4. Nom de l'entreprise :", company)
print()

# 5. Longueur
print("Exercice N°5 : Longueur de la chaîne")
print("5. Longueur de la chaîne :", len(company))
print()

# 6. En majuscules
print("Exercice N°6 : En majuscules")
print("6. Majuscules :", company.upper())
print()

# 7. En minuscules
print("Exercice N°7 : En minuscules")
print("7. Minuscules :", company.lower())
print()

# 8. Capitalisation, Titre, Inversion
print("Exercice N°8 : Capitalisation, Titre, Inversion")
print("8. Capitalize :", company.capitalize())
print("   Title :", company.title())
print("   Swapcase :", company.swapcase())
print()

# 9. Extraire le premier mot
print("Exercice N°9 : Extraire le premier mot")
print("9. Sans le premier mot :", company[7:])
print()

# 10. Vérifier si contient 'Coding'
print("Exercice N°10 : Vérifier si contient 'Coding'")
print("10. 'Coding' présent (find) :", company.find('Coding'))
print("   'Coding' présent (index) :", company.index('Coding'))
print()

# 11. Remplacer 'Coding' par 'Python'
print("Exercice N°11 : Remplacer 'Coding' par 'Python'")
print("11. Remplacement :", company.replace('Coding', 'Python'))
print()

# 12. Remplacer dans autre phrase
print("Exercice N°12 : Remplacer dans une autre phrase")
phrase = "Python for Everyone"
print("12. Remplacement :", phrase.replace('Everyone', 'All'))
print()

# 13. Split sur espace
print("Exercice N°13 : Split sur espace")
print("13. Découpage avec espace :", company.split())
print()

# 14. Split avec virgule
print("Exercice N°14 : Split avec virgule")
techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14. Découpage par virgule :", techs.split(', '))
print()

# 15. Caractère à l'index 0
print("Exercice N°15 : Caractère à l'index 0")
print("15. Caractère à l’index 0 :", company[0])
print()

# 16. Dernier index
print("Exercice N°16 : Dernier caractère")
print("16. Dernier caractère :", company[-1])
print()

# 17. Caractère à l'index 10
print("Exercice N°17 : Caractère à l'index 10")
print("17. Caractère à l’index 10 :", company[10])
print()

# 18. Acronyme de Python For Everyone
print("Exercice N°18 : Acronyme de Python For Everyone")
acronyme1 = ''.join([mot[0] for mot in "Python For Everyone".split()])
print("18. Acronyme :", acronyme1)
print()

# 19. Acronyme de Coding For All
print("Exercice N°19 : Acronyme de Coding For All")
acronyme2 = ''.join([mot[0] for mot in "Coding For All".split()])
print("19. Acronyme :", acronyme2)
print()

# 20. Position du premier C
print("Exercice N°20 : Position du premier C")
print("20. Position du 'C' :", company.index('C'))
print()

# 21. Position du premier F
print("Exercice N°21 : Position du premier F")
print("21. Position du 'F' :", company.index('F'))
print()

# 22. Position du dernier 'l' dans autre phrase
print("Exercice N°22 : Position du dernier 'l' dans une autre phrase")
long_str = "Coding For All People"
print("22. Dernier 'l' :", long_str.rfind('l'))
print()



# 23. Position du premier 'because'
print("Exercice N°23 : Position du premier 'because'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print("23. Premier 'because' (find) :", sentence.find('because'))
print()

# 24. Dernier 'because'
print("Exercice N°24 : Dernier 'because'")
print("24. Dernier 'because' (rindex) :", sentence.rindex('because'))
print()

# 25. Extraire 'because because because'
print("Exercice N°25 : Extraire 'because because because'")
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print("25. Sous-phrase extraite :", sentence[start:end])
print()

# 26. Position du premier
print("Exercice N°26 : Position du premier 'because'")
print("26. Position du premier 'because' :", start)
print()

# 27. Commence par "Coding"
print("Exercice N°27 : Commence par 'Coding'")
print("27. Commence par 'Coding' :", company.startswith('Coding'))
print()

# 28. Finit par "coding"
print("Exercice N°28 : Finit par 'coding'")
print("28. Finit par 'coding' :", company.endswith('coding'))
print()

# 29. Supprimer les espaces
print("Exercice N°29 : Supprimer les espaces")
chaine_espace = " Coding For All "
print("29. Sans espaces :", chaine_espace.strip())
print()

# 30. Vérifier si identifier
print("Exercice N°30 : Vérifier si identifiant")
print("30. identifiant 30DaysOfPython :", "30DaysOfPython".isidentifier())
print("    identifiant thirty_days_of_python :", "thirty_days_of_python".isidentifier())
print()

# 31. Joindre une liste avec "# "
print("Exercice N°31 : Joindre une liste avec '# '")
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("31. Bibliothèques Python :", ' # '.join(libs))
print()

# 32. Saut de ligne
print("Exercice N°32 : Saut de ligne")
print("32. Phrase avec retour à la ligne :\nI am enjoying this challenge.\nI just wonder what is next.")
print()

# 33. Tabulation
print("Exercice N°33 : Tabulation")
print("33. Tableau avec tabulation :")
print("Nom\tÂge\tPays\tVille")
print("Asabeneh\t250\tFinland\tHelsinki")
print()

# 34. Formatage : aire d’un cercle
print("Exercice N°34 : Formatage aire d’un cercle")
rayon = 10
aire = 3.14 * rayon ** 2
print(f"34. L’aire d’un cercle de rayon {rayon} est {aire} mètres carrés.")
print()

# 35. Calculs avec formatage
print("Exercice N°35 : Calculs avec formatage")
a, b = 8, 6
print(f"35. {a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
print()
