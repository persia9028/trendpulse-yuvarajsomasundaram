def analyze_interest_data(input_file='cleaned_interest_data.csv'):
    import pandas as pd

    df = pd.read_csv(input_file)
    df['date'] = pd.to_datetime(df['date'])
    keyword = df.columns[1]

    mean_interest = df[keyword].mean()
    max_interest = df[keyword].max()
    min_interest = df[keyword].min()

    peak_row = df[df[keyword] == max_interest]
    peak_date = peak_row['date'].values[0]

    print(f"Average interest for '{keyword}': {mean_interest:.2f}")
    print(f"Maximum interest for '{keyword}': {max_interest}")
    print(f"Minimum interest for '{keyword}': {min_interest}")
    print(f"Peak interest occurred at: {peak_date}")

    df['day'] = df['date'].dt.date
    daily_avg = df.groupby('day')[keyword].mean().reset_index()
    print("\nDaily average interest:")
    print(daily_avg)

if __name__ == "__main__":
    analyze_interest_data()
