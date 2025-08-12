 # Jour 20 : 30 Days of Python Programming

import requests
import statistics
from collections import Counter
from bs4 import BeautifulSoup


# 1. 10 mots les plus fréquents dans Roméo et Juliette
print("Exercice 1 : 10 mots les plus fréquents dans Roméo et Juliette")
def most_frequent_words(url, n=10):
    text = requests.get(url).text
    words = [w.strip(".,!?;:\"()[]").lower() for w in text.split()]
    words = [w for w in words if w.isalpha()]
    freq = Counter(words)
    return freq.most_common(n)

romeo_and_juliet_url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
print("10 mots les plus fréquents :")
print(most_frequent_words(romeo_and_juliet_url, 10))
print()

# 2. Statistiques sur les chats (Cat API)

cats_url = "https://api.thecatapi.com/v1/breeds"
cats_data = requests.get(cats_url).json()

def parse_weight(weight_str):
    """Convertit '3 - 5' en moyenne ou liste."""
    nums = [float(x) for x in weight_str.split(" - ")]
    return nums

def stats(values):
    return {
        "min": min(values),
        "max": max(values),
        "mean": round(statistics.mean(values), 2),
        "median": statistics.median(values),
        "std_dev": round(statistics.stdev(values), 2)
    }

# Poids
weights = []
lifespans = []
country_freq = Counter()

for cat in cats_data:
    w = parse_weight(cat['weight']['metric'])
    weights.extend(w)

    life = [float(x) for x in cat['life_span'].split(" - ")]
    lifespans.extend(life)

    country_freq[cat.get('origin', 'Unknown')] += 1

print("\nStatistiques poids (kg) :", stats(weights))
print("Statistiques espérance de vie (ans) :", stats(lifespans))
print("Fréquence par pays :", country_freq.most_common())


# 3. API des pays

countries_url = "https://countries-api-abhishek.vercel.app/countries"
countries_data = requests.get(countries_url).json()

# 10 plus grands pays par superficie
largest_countries = sorted(
    countries_data, key=lambda x: x.get('area', 0), reverse=True
)[:10]
print("\n10 plus grands pays :", [c['name'] for c in largest_countries])

# 10 langues les plus parlées
lang_freq = Counter()
for c in countries_data:
    for lang in c.get('languages', []):
        lang_freq[lang] += 1
print("10 langues les plus parlées :", lang_freq.most_common(10))

# Nombre total de langues
print("Nombre total de langues :", len(lang_freq))


# 4. UCI datasets avec BeautifulSoup

uci_url = "https://archive.ics.uci.edu/datasets"
html = requests.get(uci_url).text
soup = BeautifulSoup(html, "html.parser")

datasets = [a.text for a in soup.find_all("a") if a.get("href", "").startswith("/datasets/")]
print("\nNombre de datasets listés sur UCI :", len(datasets))
print("Exemples :", datasets[:10])
