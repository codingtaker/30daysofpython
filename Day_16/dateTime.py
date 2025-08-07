 # Jour 16 : 30 Days of Python Programming

from datetime import datetime


# 1. Obtenir le jour, mois, année, heure, minute et timestamp
now = datetime.now()
print("exercice 1:")
print("\nDay:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())
print()

# 2. Formater la date actuelle
print("exercice 2:")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted:", formatted_date)
print()

# 3. Convertir une chaîne "5 December, 2019" en objet datetime
print("exercice 3:")
date_str = "5 December, 2019"
converted_date = datetime.strptime(date_str, "%d %B, %Y")
print("Converted datetime:", converted_date)
print()

# 4. Calculer la différence entre maintenant et le Nouvel An
print("exercice 4:")
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)  # Nouvel An de l'année suivante
diff = new_year - now
print("Time until New Year:", diff)
print("Days left:", diff.days)
print("Seconds left:", diff.total_seconds())
print()

# 5. Calculer la différence entre 1 Janvier 1970 et maintenant
print("exercice 5:")
epoch = datetime(1970, 1, 1)
now = datetime.now()
diff_from_epoch = now - epoch
print("Since Unix Epoch:", diff_from_epoch)
print("Total seconds:", diff_from_epoch.total_seconds())
print()

# 6. À quoi peut servir le module datetime ?
"""
Le module `datetime` permet de gérer facilement les dates et heures en Python, 
notamment pour suivre le temps, planifier des événements ou enregistrer des activités.
"""