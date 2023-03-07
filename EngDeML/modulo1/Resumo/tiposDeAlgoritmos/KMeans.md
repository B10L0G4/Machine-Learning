K-Means é um algoritmo não supervisionado que agrupa os dados em K clust. 

K clust é o numero de grupos que o algoritmo deve criar.
Centroides são os pontos que representam cada clust.


Como funciona o K-means? 

Ele funciona da seguinte forma:

1. Escolhe um numero K de clusts
2. Seleciona K pontos aleatorios como centróides
3. Atribui cada ponto ao clust mais proximo do centróide
4. Calcula o novo centróide para cada clust
5. Repete os passos 3 e 4 até que os centróides não se movam mais

Como é o movimento dos centróides?

O movimento dos centróides é o seguinte:
1. O centróide se move para o centro de massa dos pontos do clust

Hiperparametros do K-means
Hiperparametros são parametros que não são aprendidos pelo modelo, mas que são definidos pelo usuario.

Para o K-means, os parametros são:
o parametro é q o algoritmo consegue aprender ao final
1. Numero de clusts
2. Numero de iterações
3. Numero de inicializações
4. medidads de distâncias

Elbow Curve  ( ou curva de cotovelo)
A curva de cotovelo é uma técnica que ajuda a escolher o numero de clusts ideal para o K-means.
Ocorre quando há um aumento brusco na distância intra-clusts e um aumento suave na distância inter-clusts.
(intra-clusts é a distância entre os pontos do clust e o centróide do clust)

Metodo Silhueta ou Silhouette Score
O metodo silhueta é uma métrica que mede a qualidade de um agrupamento.
como é calculado? 

coeficiente de silhueta = b(i) -a(i))/max (a(i),b(i)) (i = 1,2,3,4,5,6,7,8,9,10)
(a(i) = distância media do ponto i para todos os pontos do mesmo clust)
(b(i) = distância media do ponto i para todos os pontos do clust mais proximo
max (a(i),b(i)) = maior entre a(i) e b(i)

1. Para cada ponto, calcula a distância media para todos os pontos do mesmo clust
2. Calcula a distância media para todos os pontos do clust mais proximo
3. Calcula a silhueta do ponto como a diferença entre as duas distâncias dividida pela maior das duas distâncias
4. Calcula a silhueta media do agrupamento como a media das silhuetas de todos os pontos







