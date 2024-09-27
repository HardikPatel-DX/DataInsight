import pandas as pd
from src.data_cleaning import clean_data
from src.data_analysis import summary_statistics, correlation_analysis
from src.data_visualization import plot_distribution, plot_correlation_heatmap

def main():
    # Load data
    file_path = input("Enter the CSV file path: ")
    df = pd.read_csv(file_path)

    # Clean data
    df = clean_data(df)

    # Generate statistics
    print("Summary Statistics:")
    print(summary_statistics(df))

    # Correlation analysis
    print("Correlation Matrix:")
    print(correlation_analysis(df))

    # Visualize data
    plot_distribution(df)
    plot_correlation_heatmap(df)

if __name__ == "__main__":
    main()

