# KNN 

> KNN - K-Nearest Neighbors ou K-Vizinhos mais próximos é um algoritmo de aprendizado de máquina supervisionado que é usado para classificação e regressão.
> ele mede a distancia entre um ponto de teste e todos os pontos de treinamento, e atribui a classe do ponto de treinamento mais proximo ao ponto de teste.
>
> Como funciona o KNN ? 
> a classificação é feita por meio de uma votação majoritária, onde o algoritmo vota para cada ponto de teste, e o ponto de teste é classificado com a classe que recebeu mais votos.
> ele funciona da seguinte forma:
> 1. Escolhe um numero K de vizinhos
> 2. Calcula a distância entre o ponto de teste e todos os pontos de treinamento
> 3. Seleciona os K vizinhos mais próximos
> 4. Vota para cada classe
> 5. Atribui a classe com mais votos ao ponto de teste
> 
> distancia euclidiana : dist(d) = sqrt((x1-x2)^2 + (y1-y2)^2) 
    >> sqrt = raiz quadrada
    >> ^ = elevado a
    >> d = distancia
    >> x1 = coordenada x do ponto 1
    >> x2 = coordenada x do ponto 2
    >> y1 = coordenada y do ponto 1
    >> y2 = coordenada y do ponto 2
    >> ex: dist(1,2,3,4) = sqrt((1-3)^2 + (2-4)^2) = sqrt(4+4) = sqrt(8) = 2.82
>
> como escolher o valor de K ?
> o valor de K é um hiperparametro, ou seja, um parametro que não é aprendido pelo modelo, mas que é definido pelo usuario.
> o valor de K é escolhido de acordo com o problema, mas geralmente é escolhido um numero impar, para evitar empates.
> pequenos  valores de K podem causar overfitting, ou seja, o modelo pode se ajustar muito bem aos dados de treinamento, mas não generalizar bem para novos dados.
> grandes valores de K podem causar underfitting, ou seja, o modelo não se ajusta bem aos dados de treinamento.
> o ideal é escolher um valor de K que seja o menor possivel, mas que não cause underfitting.
>
> o numero de visinhos mais proximos podem ser utilizados pelo k = sqrt(n)/2, onde n é o numero de pontos de treinamento. assim podemos ter um valor de K que seja o menor possivel, mas que não cause underfitting.

> Aplicação
> O KNN é usado para classificação e regressão, ele é usado para prever a classe de um ponto de teste, baseado nos pontos de treinamento mais próximos.

