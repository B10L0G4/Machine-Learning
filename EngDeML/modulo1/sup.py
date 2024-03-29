import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importas os data sets da pasta files

df_supervi = pd.read_csv('files\iris_superv.csv')

print('HEAD',df_supervi.head(),'\n') #imprime os primeiros 5 itens do dataset 

print('TAIL',df_naoSupervi.tail(),'\n') #imprime as 5 ultimas linhas  do dataset
print('DESCRIBE_NSUP',df_naoSupervi.describe(),'\n')
print('INFO NSUP',df_naoSupervi.info(),'\n')

print('DESCRIBE',df_supervi.describe(),'\n') #imprime as estatisticas do dataset

print('INFO',df_supervi.info(),'\n') #imprime as informações do dataset
# retorna o numero de entradas (indices que há), me dá o numero total de colunas ,e nos dá os valores não nulos , e os tipos de dados que estamos trabalhando (no pandas objects sçao strings (valores textuais) ) 

print('COLUMNS',df_supervi.columns,'\n') #imprime os nomes das colunas do dataset

print('SHAPE',df_supervi.shape,'\n') #imprime a quantidade de linhas e colunas do dataset

#Construção de gráficos 
groups = df_supervi.groupby('Classe') 

#Plotando o gráfico de dispersão
fig, ax = plt.subplots()
ax.margins(0.05)

# Para cada grupo no data frame, pegue o nome e o grupo, e plote-os ( interação entre os grupos contruidos normal e sobreposto)

for name, group in groups : # name = nome do grupo , group = grupo
    ax.plot(group['Comp. Sepalas (cm)'], group['Larg. Sepalas (cm)'], marker='o', linestyle='', ms=12, label=name) 

ax.legend() #define a legenda do gráfico
plt.xlabel('Comp. Sepalas(cm)') # define o nome do eixo x
plt.ylabel('Larg. Sepalas(cm)') # define o nome do eixo y
plt.title('Comprimento e Largura das Sepalas') # define o titulo do gráfico
leg = ax.legend(loc="lower right" )# definne a localização da legenda 
#plt.show() # exibe o gráfico em uma nova janela 

df_naoSupervi.plot.scatter(x= 'Comp. Sepalas (cm)',y='Larg. Sepalas (cm)', marker= 'o')


#plt.show() # exibe o gráfico em uma nova janela

#criando um novc dataset 

df_supervi_new = df_supervi.copy() #copia o dataset para um novo dataset 

df_supervi_new['new_col']=df_supervi['Comp. Sepalas (cm)']/100 # cria uma nova coluna no dataset

print(df_supervi_new.head()) # imprie os primeiros 5 valores com a nova coluna

df_supervi_new.rename(columns={'new_col':'Comp. Sepalas (m)'},inplace=True) #renomeia a coluna criada, o onplace = true faz a alteração no dataset original

df_supervi_new.to_csv('df_modificado.csv',index=False) #salva o datset modificado em um novo arquivo csv , o index=false retira o indice do dataset. 