import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        sns.histplot(df[col], kde=True)
        plt.show()

def plot_correlation_heatmap(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.show()

