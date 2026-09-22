def clean_interest_data(input_file='interest_over_time.csv', output_file='cleaned_interest_data.csv'):
    import pandas as pd

    df = pd.read_csv(input_file)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    df = df.drop_duplicates()
    df = df[df['isPartial'] == False]
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_interest_data()
