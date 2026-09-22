def visualize_interest_data(input_file='cleaned_interest_data.csv'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.read_csv(input_file)
    df['date'] = pd.to_datetime(df['date'])
    keyword = df.columns[1]

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='date', y=keyword)
    plt.title(f'Interest Over Time for "{keyword}"')
    plt.xlabel('Date')
    plt.ylabel('Interest')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    df['day'] = df['date'].dt.date
    daily_avg = df.groupby('day')[keyword].mean().reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=daily_avg, x='day', y=keyword, palette='viridis')
    plt.title(f'Daily Average Interest for "{keyword}"')
    plt.xlabel('Day')
    plt.ylabel('Average Interest')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_interest_data()
