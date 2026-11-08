import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv(
    "comptagevelo2013.csv",
    encoding="latin1"
)

# Перетворення дати
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%Y-%m-%d"
)

# Перетворення значень у числовий формат
columns = df.columns.drop("Date")

df[columns] = df[columns].apply(
    pd.to_numeric,
    errors="coerce"
).fillna(0)

# Первинний аналіз
print("Перші рядки:")
print(df.head())

print("\nІнформація про DataFrame:")
df.info()

print("\nОписова статистика:")
print(df.describe())

# Загальна кількість велосипедистів за 2013 рік
total = df[columns].sum().sum()

print("\nЗагальна кількість велосипедистів:")
print(total)

# Вибір трьох велодоріжок
selected = [
    "Rachel / Papineau",
    "Berri1",
    "Maisonneuve_1"
]

# Групування за місяцями
monthly = df.groupby(
    df["Date"].dt.month
)[selected].sum()

print("\nКількість велосипедистів за місяцями:")
print(monthly)

# Назви місяців
months = {
    1: "Січень",
    2: "Лютий",
    3: "Березень",
    4: "Квітень",
    5: "Травень",
    6: "Червень",
    7: "Липень",
    8: "Серпень",
    9: "Вересень",
    10: "Жовтень",
    11: "Листопад",
    12: "Грудень"
}

# Найбільш популярний місяць
print("\nНайбільш популярні місяці:")

for column in selected:
    popular_month = monthly[column].idxmax()

    print(
        column,
        "-",
        months[popular_month],
        "-",
        monthly[column].max(),
        "велосипедистів"
    )

# Динаміка використання велодоріжки Maisonneuve_1
bike_path = monthly["Maisonneuve_1"]

print("\nДинаміка використання Maisonneuve_1:")
print(bike_path)

# Побудова графіка
plt.figure(figsize=(10, 5))

plt.plot(
    [months[m] for m in bike_path.index],
    bike_path.values,
    marker="o"
)

plt.title("Використання велодоріжки Maisonneuve_1 за 2013 рік")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")

plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

plt.show()

# Збереження результатів
monthly.to_csv("monthly_bicycle_analysis.csv")

print("\nРезультати збережено у CSV-файл")