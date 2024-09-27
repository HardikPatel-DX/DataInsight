from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=3):
    km = KMeans(n_clusters=n_clusters)
    df['cluster'] = km.fit_predict(df.select_dtypes(include=['float64', 'int64']))
    return df
