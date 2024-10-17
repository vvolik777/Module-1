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
