import matplotlib.pyplot as plt
import numpy as np
import json
try:
    with open("weather.json", "r", encoding="utf-8") as f:
        weather_data = json.load(f)
except FileNotFoundError:
    print("Файл 'weather.json' не знайдено.")
    exit()
# Підрахунок кількості днів
rain_days = 0
snow_days = 0
no_p_days = 0
for precip, temp in weather_data.values():
    if precip == 0:
        no_p_days += 1
    elif temp >= 0:
        rain_days += 1
    else:
        snow_days += 1
# Підготовка даних для діаграми
labels = ["Дощ", "Сніг", "Без опадів"]
counts = [rain_days, snow_days, no_p_days]
# Функція для підписів
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} днів)"
# Побудова кругової діаграми
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
colors = ['skyblue', 'lightcoral', 'lightgreen']
wedges, texts, autotexts = ax.pie( counts, autopct=lambda pct: func(pct, counts), textprops=dict(color="black"), colors=colors, startangle=90 )
ax.legend(wedges, labels,
          title="Тип опадів",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight="bold")
ax.set_title("Типи опадів за 10 днів")
plt.show()
