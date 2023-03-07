# Regressão Linear - Linear Regression

> Regressão Linear é um algoritmo supervisionado que é usado para prever valores continuos. 
>  

> - Regressão Linear Simples - é uma reta/linha, encontramos a reta que melhor se ajusta/explique aos dados ou seja encontra o coeficiente da equação da reta. 
> - É um método paramétrico , indica que há vários parametros na equação da reta. 
> - É um método deterministico , indica que o modelo é deterministico, ou seja, o modelo é determinado por um conjunto de parametros.
> a equação mais simples da reta é y = ax + b , onde a é o coeficiente angular e b é o coeficiente linear.
> erro = y - y' , onde y é o valor real e y' é o valor previsto. o erro é a diferença entre o valor real e o valor previsto. 

> Erro medio quadrarico - MSE - Mean Squared Error - é a media dos erros quadrados, ou seja, o erro ao quadrado. 
>> mse = (1/n) * sum(erro^2) , onde n é o numero de pontos de treinamento. 
>> função perda - loss function - é uma função que mede o quão ruim é o modelo, quanto menor o valor da função perda, melhor é o modelo.
>> a função perda é a mesma que o erro medio quadrarico, ou seja, o erro ao quadrado.
>> a função perda é usada para otimizar o modelo, ou seja, encontrar os parametros que minimizam o erro medio quadrarico.


> - O coeficiente angular é a inclinação da reta, e o coeficiente linear é o ponto de interseção da reta com o eixo y.Dá a inclinação na reta e o ponto de interseção com o eixo y.Intersepto é o ponto onde a reta cruza o eixo y.encontra o valor de a e b que  minimiza o erro entre o valor real e o valor previsto.

> por exemplo: y = 2x + 3 , a = 2 e b = 3

> Como encontramos o valor da combinação 
> metodo gradiente descendente - gradient descent - é um algoritmo de otimização que é usado para encontrar os parametros que minimizam a função perda.descendente pos vai no sentido contrario do gradiente, ou seja, vai na direção oposta do gradiente.

> as validações são feitas em treinmaneto e teste, ou seja, o modelo é treinado com os dados de treinamento e testado com os dados de teste.

> não usamos as premissas estatisticas, aleatoriedade e independencia.
> premissas estatisticas - statistical assumptions - são premissas que são feitas para que o modelo funcione bem.
>aleatoriedade - random - é uma premissa que indica que os dados são aleatorios, ou seja, não há uma ordem nos dados.
>independencia - independency - é uma premissa que indica que os dados são independentes, ou seja, um dado não influencia no outro.

### Quando e pq utilizar 
>
> Sempre que possivel, é bom utilizar o modelo de regressão linear, pois é um modelo simples e fácil de entender.
> problemas lineares são problemas que podem ser resolvidos com uma reta, ou seja, problemas que podem ser resolvidos com uma equação de reta.

> Cuidados com underfiting quando o modelo não seja exatamente linear e overfiting quando o modelo seja muito complexo.

> Facil compreensão e interpretação dos resultados.