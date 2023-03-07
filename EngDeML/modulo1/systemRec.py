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

#plt.show()# plota os dados em uma nova janela 

# Construção de matriz de relacionamento entre os filmes e os usuários

movie_rating_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating') #cria uma matriz com os dados de avaliação dos filmes, onde matrix é o nome da matriz, pivot_table é uma função que cria uma matriz, index='userId' define a coluna que será usada como index, columns='title' define a coluna que será usada como coluna, values='ratings' define a coluna que será usada como valores

movie_rating_matrix.tail() #mostra os ultimos dados da matriz

movie_corr_matrix =movie_rating_matrix.corr()  #cria uma matriz de correlação entre os filmes, onde movie_corr_matrix é o nome da matriz, corr() é uma função que cria uma matriz de correlação
movie_corr_matrix.head()

#refina matriz de correlação 
movie_corr_matrix = movie_rating_matrix.corr(method='pearson', min_periods=50) #utiliza o metodo de pearsonpara gerar a correlação.
# method='pearson' define o método de correlação, min_periods=50 define a quantidade mínima de avaliações que um filme deve ter para ser considerado na matriz de correlação

# essas analises são feitas para encontrar filmes similares , avaliando a correlação entre os filmes
# exemplo: se um filme tem uma correlação de 0.5 com outro filme, significa que as pessoas que gostaram de um filme também gostaram do outro filme

print(movie_rating_matrix.shape) # mostra a quantidade de linhas e colunas da matriz

testUser = movie_rating_matrix.iloc[600].dropna() 
print(testUser.head(10).sort_values(ascending=False)) #mostra os 10 filmes com maior avaliação do usuario 600

len(testUser)   #mostra a quantidade de filmes que o usuario 600 avaliou
testUser.index[2]# mostra o nome do filme 2 do usuario 600

testUser[2]# mostra a avaliação do filme 2 do usuario 600

print(movie_corr_matrix[testUser.index[2]].dropna().sort_values(ascending=False))  
# mostra os 10 filmes com maior correlação com o filme 2 do usuario 600)] #encontrando os filmes similares ao filme 2 do usuario 600

similarMoviesCandidatos = pd.Series() #cria uma serie vazia
for i in range(0, len(testUser.index)):
    print("Analisando o filme: " +testUser.index[i]+ "...")
    similar = movie_corr_matrix[testUser.index[i]].dropna()
    similar=similar.map(lambda x : x*testUser[i]) #multiplica a correlação do filme pelo valor da avaliação do filme
    similarMoviesCandidatos = similarMoviesCandidatos.append(similar) #adiciona os filmes similares a serie vazia

    #similarMoviesCandidatos = similarMoviesCandidatos.append(movie_corr_matrix[testUser.index[i]].dropna(), ignore_index=True) #adiciona os filmes similares a serie vazia

similarMoviesCandidatos.sort_values(inplace=True, ascending=False)# ordena os filmes similares

print(similarMoviesCandidatos.head(15))  #mostra os 10 filmes similares com maior correlação

similarMoviesCandidatos=similarMoviesCandidatos.groupby(similarMoviesCandidatos.index).sum() #agrupa os filmes similares e soma a correlação
similarMoviesCandidatos.sort_values(inplace=True, ascending=False) #ordena os filmes similares
similarMoviesCandidatos.head(10) #mostra os 10 filmes similares com maior correlação

filtra_movies = similarMoviesCandidatos[~similarMoviesCandidatos.index.isin(testUser.index)] #filtra os filmes similares que o usuario já avaliou
filtra_movies.head(10) #mostra os 10 filmes similares com maior correlação
filme = ['12 Angry Men(1957'] #define o nome do filme
filme in list(testUser) #verifica se o filme já foi avaliado pelo usuario

filtra_movies_recomendations=filtra_movies.sort_values(ascending=False) #ordena os filmes similares
print(filtra_movies_recomendations.head(50)) #mostra os 50 filmes similares com maior correlação
