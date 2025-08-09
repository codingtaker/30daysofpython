 # Jour 18 : 30 Days of Python Programming


from collections import Counter
import re

"""

Exercices 1:

"""
#1. Trouver le mot le plus fréquent dans le paragraphe
print("exercice 1.1:")
paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.'''

words = re.findall(r'\w+', paragraph.lower())
word_counts = Counter(words)

sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print(sorted_counts)
print()

#2. Trouver la distance maximale entre deux particules
print("exercice 1.2:")
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in
the negative direction, 0 at origin, 4 and 8 in the positive direction."""

points = list(map(int, re.findall(r'-?\d+', text)))
distance = max(points) - min(points)

print("Points :", points)
print("Distance maximale :", distance)

"""

Exercices 2:

"""
print("\nExercice 2:")
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_]\w*$'
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname')) 

"""

Exercices 2:

"""
# 3. Nettoyer le texte et trouver les mots les plus fréquents
print("\nExercice 3:")
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

# Fonction pour nettoyer le texte
def clean_text(text):
    return re.sub(r'[^A-Za-z\s]', '', text)

cleaned_text = clean_text(sentence)

def most_frequent_words(text):
    words = re.findall(r'\w+', text)
    counter = Counter(words)
    return counter.most_common(3)

print(cleaned_text)
print(most_frequent_words(cleaned_text))