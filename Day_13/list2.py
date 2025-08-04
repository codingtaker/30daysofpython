 # Jour 13 : 30 Days of Python Programming


#1. Filtrer les nombres négatifs et zéro

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print(neg_and_zero)

# 2. Aplatir une liste de listes de listes

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist in list_of_lists for item in sublist[0]]
print(flattened)

# 3. Générer une liste de tuples avec compréhension de liste

tuples_list = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuples_list)
# 4. Transformer la liste de pays en liste formatée

countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [[country.upper(), country[:3].upper(), city.upper()]
                  for [[(country, city)]] in countries]
print(flat_countries)


[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# 5. Transformer en liste de dictionnaires

country_dicts = [{'country': country.upper(), 'city': city.upper()}
                 for [[(country, city)]] in countries]
print(country_dicts)
# 6. Transformer en liste de chaînes concaténées

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[(first, last)]] in names]
print(full_names)
# ➜ ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# 7. Fonction Lambda pour slope ou y-intercept

# Slope = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# y-intercept = y - mx
y_intercept = lambda m, x, y: y - m * x


print("Slope :", slope(2, 2, 6, 10))
print("Y-intercept :", y_intercept(2, 2, 2))