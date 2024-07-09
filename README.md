# Análise de Filtragem de Dados de Partidas de League of Legends

## Introdução

Este projeto compara duas abordagens para filtrar dados de partidas de um jogador em League of Legends, com o objetivo de obter um conjunto de dados mais homogêneo. As duas abordagens são:

1. Filtragem baseada no Desvio Padrão
2. Filtragem baseada no K-means Clustering

## Dados

Os dados consistem em registros de partidas de League of Legends, incluindo informações como data, campeão jogado, número de abates, mortes, assistências, entre outros.

## Abordagens de Filtragem

### 1. Filtragem baseada no Desvio Padrão

Nesta abordagem, calculamos a média e o desvio padrão do KDA (abates + assistências / mortes) e filtramos os dados para manter apenas os valores dentro de uma faixa de desvio padrão definida em torno da média.

#### Resultados

- **Número de linhas antes da filtragem**: 30
- **Média do KDA**: 5.6681
- **Desvio padrão do KDA**: 7.1074
- **Número de linhas depois da filtragem**: 8

```plaintext
date               champion  kills  deaths  assists  KDA
2023-11-16 05:35:36.539  Jhin        20     5       13      6.600000
2023-11-16 04:24:53.256  Jhin         4     4       12      4.000000
2023-11-16 03:29:44.830  TwistedFate  2     4       18      5.000000
2023-11-16 02:35:01.656  KogMaw      10     6       21      5.166667
2023-11-15 23:39:30.830  TwistedFate  4     4       13      4.250000
2023-11-15 23:11:49.646  Nami         0     5       20      4.000000
2023-11-15 22:39:35.486  Jhin         6     3       15      7.000000
2023-11-15 19:19:32.776  Nami         3     5       18      4.200000

### 2. Filtragem baseada em K-means Clustering

Nesta abordagem, aplicamos o algoritmo K-means para identificar clusters de valores de KDA e filtramos os dados para manter apenas o cluster principal, seguido de uma filtragem adicional baseada no desvio padrão dentro do cluster principal.

#### Resultados
- **Número de linhas antes da filtragem**: 30
- **Número de linhas depois da filtragem**: 13

```plaintext
date               champion  kills  deaths  assists  KDA
2024-02-11 18:26:36.425  Yasuo       12     4        2      3.500000
2023-11-16 04:53:41.714  Brand       10     9       18      3.111111
2023-11-16 04:24:53.256  Jhin         4     4       12      4.000000
2023-11-16 03:29:44.830  TwistedFate  2     4       18      5.000000
2023-11-16 02:35:01.656  KogMaw      10     6       21      5.166667
2023-11-16 00:07:06.784  Jhin         5     4        7      3.000000
2023-11-15 23:39:30.830  TwistedFate  4     4       13      4.250000
2023-11-15 23:11:49.646  Nami         0     5       20      4.000000
2023-11-15 22:16:44.482  Jhin         2     3        7      3.000000
2023-11-15 21:43:21.713  TwistedFate  4     5       14      3.600000
2023-11-15 21:17:38.538  Jhin         7     5       10      3.400000
2023-11-15 20:14:54.764  Jhin         9     7       18      3.857143
2023-11-15 19:19:32.776  Nami         3     5       18      4.200000

## Conclusão

- **Desvio Padrão**: Eficaz, mas pode manter partidas com KDAs extremos, especialmente quando o desvio padrão é alto.
- **K-means**: Proporciona uma melhor homogeneidade, mantendo partidas com KDAs mais próximos entre si.

A abordagem baseada em K-means parece ser mais apropriada para obter um conjunto de dados mais consistente e homogêneo.

## Execução do Projeto

### Requisitos

- Python 3.x
- Pandas
- Scikit-learn

### Instalação

1. Crie um ambiente virtual:
   ```sh
   python3 -m venv venv
   ```

2. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. Instale as dependências:
   ```sh
   pip install pandas scikit-learn
   ```

### Execução

1. Execute os scripts:
   ```sh
   python lol-sd.py
   python lol-kmeans.py
   ```
