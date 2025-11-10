import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import csv
# Масиви даних
x = []   # роки
y = []   # Україна
z = []   # Велика Британія
# Читання CSV
with open("Data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row["Country Name"].strip()
        for key, val in row.items():
            if key.startswith("20") and val not in ("", ".."):
                try:
                    year = int(key[:4])
                    value = float(val)
                except ValueError:
                    continue
                if country == "Ukraine":
                    x.append(year)
                    y.append(value)
                elif country == "United Kingdom":
                    z.append(value)
# 2.1
plt.plot(x, y, label='Ukraine', color = "red")
plt.plot(x, z, label=' United Kingdom', color = "green")
plt.title('Individuals using the Internet (% of population), 2003–2023', fontsize=14)
plt.xlabel('Рік', fontsize=12, color='darkred')
plt.ylabel('Відсоток користувачів Інтернету', fontsize=12, color='darkred')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(x, rotation=45)
plt.show()
# 2.2
country = input("Введіть країну для стовпчастої діаграми (Ukraine або United Kingdom): ").strip().lower()
if country == "ukraine":
    data = y
    color = "red"
elif country in ["united kingdom", "uk"]:
    data = z
    color = "green"
else:
    print("Помилка, введіть 'Ukraine' або 'United Kingdom'.")
    exit()
# Індекс для стовпців
x_bar = range(len(data))
ax = plt.gca()
ax.bar(x_bar, data, align='edge', color=color)
ax.set_xticks(x_bar)
ax.set_xticklabels(x, rotation=45)
# Підписи та заголовок
ax.set_xlabel("Рік", fontsize=12)
ax.set_ylabel("% населення", fontsize=12)
ax.set_title(f"Individuals using the Internet — {country.title()}", fontsize=15)
plt.show()