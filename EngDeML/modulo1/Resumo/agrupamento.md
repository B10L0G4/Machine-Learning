
### Agrupamento  
>  - Agrupamento: são estratégias não supervisionadas, ou seja, não temos uma saída definida, possui grupos com caracteristicas semelhantes.Não possui labels (classes) definidas  
>  - Tipos de Agrupamentos : 
>> - Hard Cluster - cada instancia pertence a um Cluster
>> - Soft Cluster - cada instancia é assosciada uma probabilidade de pertencer a um cluster 
>  - Tipos de Algoritmos: 
>> - Baseado em centroides: as condições iniciais são definidas aleatoriamente , e os centroides são atualizados iterativamente até que a convergencia seja atingida.  
>> - Baseado em densidade : define o contorno das regiões de maior densidade (menos sensivél a aoutliers)
>> - Baseado em distribuição: cada conjunto é definido por uma distribuição de probabilidade (Gaussianas, Multinomiais, etc) 
>> - Baseado em hierarquia: criado a partir de arvores hierarquicas (dendogramas) 
>> - Baseado em modelo :  
>> - Baseado em rede, 
>> - Baseado em particionamento, 
>> - Baseado em representação,
>> -  Baseado em vizinhança.
>>  - k Means : é um algoritmo de agrupamento baseado em centroides, que agrupa os dados em k grupos, onde k é um número inteiro especificado pelo usuário. 
>>  -Mean Shift cluster: funcionada a partir do conceito de subida de montanha (hill climbing), onde o algoritmo tenta encontrar o ponto mais alto da montanha.Vai englobando os pontos mais proximos até que não haja mais pontos para serem agrupados. 
>>  - DBScan - Density Based Spatial Clustering of Applications with Noise, é um algoritmo de agrupamento baseado em densidade, que agrupa os dados em clusters de alta densidade, separados por regiões de baixa densidade.A medida que ele caminha pela base de dados, ele vai agrupando os pontos mais proximos até que não haja mais pontos para serem agrupados
>>- Agrupamento Hierarquico: é um algoritmo de agrupamento baseado em hierarquia, que agrupa os dados em clusters de acordo com a similaridade entre os dados.Passa de um conjunto  menor (maior granularidade) ate chegar no conjunto com maior similaridade.
>
> - Aplicações: Sistemas de recomendação , Segmentação de Clientes, Segmentaçãi de imagens, Detecção de anomalias, Detecção de Frauedes. 

