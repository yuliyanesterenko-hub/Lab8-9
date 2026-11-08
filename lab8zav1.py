import pandas as pd
import requests

# Завантаження даних
df = pd.read_csv("exports.csv")

# Отримання додаткових показників зі Світового банку
countries = {
    "Ukraine": "UKR",
    "United States": "USA"
}

def get_data(indicator, column_name):
    data = []

    for country, code in countries.items():
        url = f"https://api.worldbank.org/v2/country/{code}/indicator/{indicator}?date=2015:2023&format=json&per_page=100"
        response = requests.get(url)
        result = response.json()

        for item in result[1]:
            data.append({
                "Country": country,
                "Year": int(item["date"]),
                column_name: item["value"]
            })

    return pd.DataFrame(data)

population = get_data("SP.POP.TOTL", "Population")
gdp = get_data("NY.GDP.PCAP.CD", "GDP_per_capita")

# Об'єднання даних
df = df.merge(population, on=["Country", "Year"])
df = df.merge(gdp, on=["Country", "Year"])

# Виведення початкового DataFrame
print("Початкові дані:")
print(df)

# Перші 3 рядки
print("\nПерші 3 рядки:")
print(df.head(3))

# Типи даних
print("\nТипи даних:")
print(df.dtypes)

# Розмір DataFrame
print("\nРозмір DataFrame:")
print(df.shape)

# Описова статистика
print("\nОписова статистика:")
print(df.describe())

# Додавання розрахункового стовпця
df["Exports_value"] = (
    df["Exports of goods and services (% of GDP)"] / 100
    * df["GDP_per_capita"] * df["Population"]
)

print("\nDataFrame з новим стовпцем:")
print(df)

# Фільтрація: експорт більше 20%
filtered_df = df[
    df["Exports of goods and services (% of GDP)"] > 20
]

print("\nРезультат фільтрації:")
print(filtered_df)

# Сортування за показником експорту
sorted_df = df.sort_values(
    by="Exports of goods and services (% of GDP)",
    ascending=False
)

print("\nРезультат сортування:")
print(sorted_df)

# Групування за країнами
grouped_df = df.groupby("Country")[
    "Exports of goods and services (% of GDP)"
].agg(["mean", "max", "min"])

print("\nРезультат групування:")
print(grouped_df)

# Кількість унікальних країн
print("\nКількість унікальних країн:")
print(df["Country"].nunique())

# Збереження результатів
df.to_csv("exports_analysis.csv", index=False)

print("\nРезультати збережено у файл exports_analysis.csv")