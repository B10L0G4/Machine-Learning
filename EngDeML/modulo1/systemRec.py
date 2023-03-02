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

# Construção de matriz de relacionamento entre os filmes e os usuários

movie_rating_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='ratings') #cria uma matriz com os dados de avaliação dos filmes, onde matrix é o nome da matriz, pivot_table é uma função que cria uma matriz, index='userId' define a coluna que será usada como index, columns='title' define a coluna que será usada como coluna, values='ratings' define a coluna que será usada como valores

movie_rating_matrix.tail() #mostra os ultimos dados da matriz

movie_corr_matrix =movie_rating_matrix.corr()  #cria uma matriz de correlação entre os filmes, onde movie_corr_matrix é o nome da matriz, corr() é uma função que cria uma matriz de correlação
movie_corr_matrix.head()

#refina matriz de correlação 
movie_corr_matrix = movie_rating_matrix.corr(method='pearson', min_periods=50) #utiliza o metodo de pearsonpara gerar a correlação.
# method='pearson' define o método de correlação, min_periods=50 define a quantidade mínima de avaliações que um filme deve ter para ser considerado na matriz de correlação




