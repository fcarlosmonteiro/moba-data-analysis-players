import pandas as pd

#filtragem com standard deviation

file_path = 'data.csv'
data = pd.read_csv(file_path)

print(f"Número de linhas antes da filtragem: {len(data)}")

data = data[data['deaths'] > 0]

# Calcular o KDA para cada partida
data['KDA'] = (data['kills'] + data['assists']) / data['deaths']

# Calcular a média e o desvio padrão do KDA
mean_kda = data['KDA'].mean()
std_kda = data['KDA'].std()

print(f"Média do KDA: {mean_kda}")
print(f"Desvio padrão do KDA: {std_kda}")

# Definir os limites de filtragem (0.25 desvio padrão da média)
lower_bound = mean_kda - 0.25 * std_kda
upper_bound = mean_kda + 0.25 * std_kda

filtered_data = data[(data['KDA'] >= lower_bound) & (data['KDA'] <= upper_bound)]

print(f"Número de linhas depois da filtragem: {len(filtered_data)}")

print(filtered_data)
#filtered_data.to_csv('filtered_matches_refined_std_v3.csv', index=False)
