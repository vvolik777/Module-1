import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fetch_data():
    print("Fetching data with requests...")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    for post in data[:5]:
        print(f"Title: {post['title']}")


def analyze_data():
    print("\nAnalyzing data with pandas...")
    df = pd.read_csv('/Users/vasilisa/Python/Module-1/Module-11/data.csv')
    print(df.info())
    average = df['age'].mean()
    print(f"Средний возраст: {average}")


def plot_data():
    print("\nVisualizing data with matplotlib...")
    data = np.random.randint(1, 100, size=100)
    plt.hist(data, bins=10, color='blue', alpha=0.7)
    plt.title("Random Data Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    fetch_data()
    analyze_data()
    plot_data()

# Библиотека requests:
# - Позволяет отправлять HTTP-запросы (GET, POST и т.д.) с минимальными усилиями
# - Обрабатывает ответы от веб-сайтов в формате JSON, что облегчает работу с API
# - Упрощает задачу извлечения данных из удаленных источников

# Расширение возможностей Python: С помощью requests Python может легко взаимодействовать с внешними API и
# получать данные из интернета, что делает его мощным инструментом для разработки веб-приложений и интеграции с другими сервисами.

# Библиотека pandas:
# - Обеспечивает удобные структуры данных (DataFrame и Series) для работы с табличными данными
# - Позволяет считывать данные из различных форматов (CSV, Excel, SQL и т.д.) и легко выполнять операции анализа данных,
# такие как фильтрация, группировка и агрегация
# - Предоставляет мощные инструменты для статистического анализа и визуализации

# Расширение возможностей Python: pandas позволяет обрабатывать и анализировать большие объемы данных с минимальными усилиями,
# делая Python отличным выбором для анализа данных и машинного обучения.

# Библиотека matplotlib:
# - Позволяет визуализировать данные с помощью различных графиков и диаграмм (линейные, столбчатые, круговые и т.д.)
# - Обеспечивает высокую гибкость в настройке внешнего вида графиков, включая цвета, метки и легенды
# - Позволяет создавать интерактивные графики для веб-приложений и отчетов

# Расширение возможностей Python: matplotlib делает Python мощным инструментом для визуализации данных, что помогает
# лучше интерпретировать результаты анализа и представлять их в наглядной форме.