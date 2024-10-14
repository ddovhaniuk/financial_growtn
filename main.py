import math
from prettytable import PrettyTable

# Функція для обчислення складного відсотка
def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    return amount

# Запитуємо у користувача вхідні дані
principal = float(input("Введіть початкову суму інвестиції: "))
rate = float(input("Введіть річну процентну ставку (%): "))
time = int(input("Введіть кількість років: "))
n = int(input("Введіть кількість періодів нарахування відсотків на рік: "))

# Розраховуємо кінцеву суму та накопичення за кожен рік
final_amount = calculate_compound_interest(principal, rate, time, n)
yearly_amounts = [calculate_compound_interest(principal, rate, t, n) for t in range(1, time + 1)]

# Виводимо результати у вигляді таблиці
table = PrettyTable()
table.field_names = ["Рік", "Накопичена сума"]

for year in range(1, time + 1):
    table.add_row([year, f"{yearly_amounts[year - 1]:.2f}"])

print("\nРезультати розрахунків:")
print(table)

# Виводимо загальну накопичену суму
print(f"\nКінцева сума після {time} років: {final_amount:.2f}")
