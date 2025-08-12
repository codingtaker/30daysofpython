 # Jour 21 : 30 Days of Python Programming

"""

Exercices 1:

"""

from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        freq = Counter(self.data)
        mode_val, count = freq.most_common(1)[0]
        return (mode_val, count)

    def var(self):
        mean_val = self.mean()
        return round(sum((x - mean_val) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        total = self.count()
        return sorted([(round((count / total) * 100, 1), value) for value, count in freq.items()],
                      reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", self.var())
        print("Standard Deviation:", self.std())
        print("Frequency Distribution:", self.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()
print()

"""

Exercices 2:

"""

print("Exercice 2:")
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {} 
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"{self.firstname} {self.lastname} | Solde: {self.account_balance()}"

person = PersonAccount("John", "Doe")
person.add_income("Salaire", 3000)
person.add_income("Freelance", 1200)
person.add_expense("Loyer", 800)
person.add_expense("Courses", 250)

print(person.account_info())
print("Total revenus :", person.total_income())
print("Total dépenses :", person.total_expense())