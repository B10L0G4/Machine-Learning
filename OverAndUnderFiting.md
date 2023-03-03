 ## Overfiting, Underfiting e modelo balanceado 
>
>  -  O que Overfitting ?
>     - Ocorre quando o modelo se ajusta muito bem aos dados de treinamento, mas não generaliza bem para dados novos.
>     - Repesenta o sobreajuste do modelo a um conjunto de dados . 
>     - Leva a perda da capacidade de generalizar novos dados.  
>     - Ele memoriza algumas instancias do treinamento e quando é apresentado a novos conjuntos ele não consegue generalizar. 
>
>> ### **Como evitar o Overfitting**? 
>   - Dividir os dados de treinamento e teste (80% - 20%)
>   - Cross-Validation ( validação cruzada), é um método de avaliação de modelos que consiste em dividir o conjunto de dados em k partesm treinar o modelo em k-1 partes e testar em uma parte.  
>   - Regularização, é um mérodo que impõe uma penalidade aos coeficientes do modelo reduzindo a complexidade do modelo.
>   - Remover neuronios/camadas de redes neurais (dropout), é um método que consiste em remover aleatoriamente alguns neuronios de uma rede neural durante o treinamento.
>   - Aplicar a 'parada precoce'( early stopping)é um método que consiste em parar o treinamento quando o modelo não aprensemta mais melhora no conjunto de vakidação.
>  ### **O que Underfiting**? 
>> - A tarefa possui maior complexidade de que o modelo é capaz de resolver. 

>  -Modelo Balanceado 
>> - o modelo deve apresentar um resukltado adequado e possui capacidade generalizada para novos dados. 

> **O dilema BIAS e VARIANCIA**
>>- O BIAS é diferença entre o valor esperado do modelo e o valor correto. 
>> - Variancia é a variação do modelo para um conjunto de dados. 
> O que é dilema de bias e variancia,  é o conflito entre o erro de bias e o erro de variancia. Qaundo é o bias é baixo a variancia é alta e vice versa, sempre que um é baixo um é alto e será necessario um tradeoff entre eles ( tradeoff é a troca de um por outro)

Quando iniciar um projeto de machine learning, é importante ter em mente que o modelo que você está construindo deve ser capaz de generalizar bem para novos dados. Isso significa que o modelo deve ser capaz de aprender padrões dos dados de treinamento e aplicá-los a novos dados. Se o modelo não for capaz de generalizar bem, ele não será útil para a tarefa que você está tentando resolver.
Começar por modelos mais simples e ir aumentando a complexidade do modelo até que o modelo comece a apresentar a resolução do problema , não esperar chegar a um overfiting , pois caso ocorra o modelo precisará ser reajustado. 
O idela é que o modelo apresente um resultado adequado e possui capacidade generalizada para novos dados ou best fit. 
