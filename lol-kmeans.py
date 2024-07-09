import pandas as pd
from sklearn.cluster import KMeans

file_path = 'data.csv'
data = pd.read_csv(file_path)

print(f"Número de linhas antes da filtragem: {len(data)}")

data = data[data['deaths'] > 0]

# Calcular o KDA para cada partida
data['KDA'] = (data['kills'] + data['assists']) / data['deaths']

# Aplicar o algoritmo K-means para identificar o cluster principal
kmeans = KMeans(n_clusters=5, random_state=0).fit(data[['KDA']])
data['Cluster'] = kmeans.labels_

main_cluster = data['Cluster'].value_counts().idxmax()

filtered_data = data[data['Cluster'] == main_cluster]

print(f"Número de linhas depois da filtragem: {len(filtered_data)}")

print(filtered_data)
#filtered_data.to_csv('filtered_matches_refined_kmeans_v2.csv', index=False)
