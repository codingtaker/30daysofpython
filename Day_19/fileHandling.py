 # Jour 19 : 30 Days of Python Programming


"""

Exercices 1:

"""
import json
from collections import Counter
import re

#1. Compter lignes et mots dans un fichier texte
print("Exercice 1.1:")
def count_lines_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count

files = [
    "data/obama_speech.txt",
    "data/michelle_obama_speech.txt",
    "data/donald_speech.txt",
    "data/melina_trump_speech.txt"
]

for file in files:
    lines, words = count_lines_words(file)
    print(f"{file} → {lines} lignes, {words}plus parlées mots")
print()

#2. Trouver les langues les
print("Exercice 1.2:")
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    languages = []
    for country in countries:
        languages.extend(country.get('languages', []))

    language_counts = Counter(languages)
    return language_counts.most_common(top_n)
print()

#3. Trouver les pays les plus peuplés
print("Exercice 1.3:")
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    sorted_countries = sorted(
        countries, key=lambda x: x.get('population', 0), reverse=True
    )
    return [
        {"country": c["name"], "population": c["population"]}
        for c in sorted_countries[:top_n]
    ]
print(most_populated_countries("data/countries_data.json", 10))
print(most_populated_countries("data/countries_data.json", 3))


"""

Exercices 2:

"""

# 4. Extraire toutes les adresses e-mail entrantes
print("\nExercice 2.1:")
def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Expression régulière pour capturer les e-mails
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
    return emails

emails_list = extract_emails("data/email_exchange_big.txt")
print(emails_list)
print()

#5. Trouver les mots les plus fréquents
print("Exercice 2.2:")
def find_most_common_words(file_or_text, top_n):
    try:
        with open(file_or_text, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        text = file_or_text
    # On nettoie le texte pour ne garder que les mots
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    word_counts = Counter(words)
    return word_counts.most_common(top_n)
print(find_most_common_words("data/sample.txt", 10))
print(find_most_common_words("data/sample.txt", 5))