# Prática para criação de um sistema de recomendação, criar um conjunto de filmes que serão atribuidas a um usuario

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_movies= pd.read_csv('./files/movies.csv')
df_ratings = pd.read_csv('./files/ratings.csv')

movie_ratings =pd.merge(df_movies, df_ratings, on='movieId') # merge , combina dois dataframes em um

#encontra amedia atribuida a cada filme 
movie_ratings.groupby('title')['rating'].mean().sort_values(ascending=False).head() # agrupa por titulo e calcula a média de avaliação 

#conta a quantidade de notas que cada filme recebeu 
movie_ratings.groupby('title')['rating'].count().sort_values(ascending=False).head()  # agrupa por titulo e conta a quantidade de avaliações 

#cria um novo dataframe que vai contar o nome de cada filme e a média de avaliação
ratings = pd.DataFrame(movie_ratings.groupby('title')['rating'].mean()) 
#(.DataFrama cria um novo dataframe)
#rating é o nome da coluna 

ratings.sort_values(by = 'rating', ascending=False).head() #ordena os filmes por avaliação

#adiciona a coluna que contêm a quantitade de notas que cada um dos filmes recebeu
ratings['num of ratings']= pd.DataFrame(movie_ratings.groupby('title')['rating'].count())
ratings.sort_values(by = 'num of ratings', ascending=False).head() #ordena os filmes por quantidade de avaliações
#num of ratings é o nome da coluna

ratings.sort_values(by = 'rating', ascending=False).head() #ordena os filmes por avaliação
#ascending=False, ordena do maior para o menor

ratings.boxplot(column='rating' ); #cria um boxplot para avaliar a distribuição das avaliações
#boxplot é um gráfico que mostra a distribuição de dados através de quartis

plt.figure(figsize=(10,4)) #cria um histograma para avaliar a distribuição das avaliações
#figsize=(10,4) define o tamanho da janela

ratings['rating'].hist(bins=70) 
#bins=70 define a quantidade de barras do histograma

plt.show()# plota os dados em uma nova janela 



