# Introdução ao Machine Learning 

## Fundamentos de Machine Learning 

> ### O que é Machine Learning ?
>
> - **Machine Learnign(ML)** ou aprendizado de maquina são algoritmos que aprendem com a experiencia ou seja com os dadso fornecidos.
> - Pode ser definido também como o estudo sistemático de algoritmos e sistemas , que melhroam o conhecimento e performance com a experiencia. 
> - É o campo de estudo que dá ao computador a habilidade de aprender sem ser explicitamente programado. Arthur Samuel, 1959
> - Utiliza um conjunto de ferramentas para modelagem de dados denominados desenvolvimento estatistico de modelos capazes de aprender a parir de dados e prever resultados 

> ### O que é aprendizado? 
> - Aprendizado é o processo de adiquirir conhecimento ou habilidade por meio de estudo, experiencia ou instrução.
> - Aprendizado para um programa são caracteristicas que o algoritmo consegue identificar e generalizar o aprendizado para entrgar a resposta esperada para um problema. 
>>#### Quando usar machine learning?
>> - Quando o problema é complexo e não tem uma solução simples ou clara. 
>>#### Quando não usar machine learning?
>> - Quando o problema é simples e tem uma solução clara.

### As variavies que compõem um problema de machine learning 
> 
>  - Variaveis de entrada (features)
>  - Dados de treinamento
>  - Algoritimo de aprendizado
>  - Função de custo
>  - Função de predição

### Tipos de Aprendizado 
>  - Aprendizado Supervisionado : recebe dados rotulados e aprende a prever a saida para novos dados. Recebe entrada.Apresenta conjuntos de instâncias/valores para que o modelo aprenda.   
> - Aprende conceitos, recebe instruções e a partir das informações recebidas/aprendidas, quando essas informações são informadas ele consegue identificar as caracteristicas a partir do aprendizado previo. 

>  - Aprendizado não Supervisionado:  não recebe dados roptulados e aprende a estruturar os dados.Não recebe entrada ou saída.Não recebe labels. Ele identifica a partir dos dados e identifica as caracteristicas distintas. 

>  - Aprendizado por reforço: recebe uma recompensas, é inserido em um ambiente e aprende a tomar ações que maximizam a recompesa. 

O que buscamos quando com uma aplicação de ML?
  Resolver uam tarefa com a melhor assertividade possivél.
  O modelo deve ser capaz de se adaptar a novos dados 
  O modelo deve ser capaz de generalizar a partir dos dados de treinamento. (treinar um modelo é ajusatar os parametros do modelo para que ele se adeque aos dados de treinamento.)

>  ## Overfiting, Underfiting e modelo balanceado 
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



### Tipos de Aprendizado 
> - 
>  - 
>  - 
>  - 
>  - 
>  -

## **História** : 

> De 1913 a 1980 (o aprendizado de maquina foi um campo de estudo que se desenvolveu em paralelo com a inteligencia artificial.)
>
>> - Deu inicio em 1913 com as cadeias de Markov propos um modelo matematico de previsão de estados , ou seja ele aprende com o passado e preve o futuro. Ele uso apenas o estado anterior para prever o proximo estado. 
>> - Em 1920 o matematico Norbert Wiener propôs o conceito de aprendizado de maquina. -- verificar 
>> - Em 1936 Alan Turing propos o artigo 'On Computer Number "que aprenseta o conceito de uma maquina que poderia resolver qaulquer problema matematico. 
>> - Em 1948 Waren McCullock e Walter Pitts propuseram o modelo de neuronio artificial, ele modelaram uma rede neural simples usando circuitos eletricos. 
>> -  Em 1952 Arthut Samuel propos p modelo computacional que aprende a jogar damas. 
>> -  1956 o termo Integencia Artificial pela primeira vez foi usado na conferencia realizada por John MacCarthy
>> - Perceptron - 1958 - Frank Rosenblatt cria o primeiro modelo matematico que corresponde a primeira rede neural artificial . 
>> - 1967 - algoritimo do vizinho mais próximo , Cover e Hart empregam o reconhecimento de padrões para classificar objetos. 
>> - 1969 - MArvim Minsky e Seymar Popert apresentam as limitações do Perceptron.
>> - Em 1982 John Hopfield props o modelo de rede neural de memoria , mostrando como adicionar memoria a uma rede neural. 

### 1990 - 2014 

>> - 1990 - Robert Schapire mostra bases para o desenvolvimento de algoritmos mais capazes de fazer Boosting (Aumento de desempenho). Metodos ensemble juntam metodos mais simples para formar um metodo mais complexo. 
>> - Em 1995 Tin Kan Leee apresenta a primera representação de Ramdom Forest , um metodo de ensemble que usa arvores de decisão. Ainda em 1995 Corinna Cortes e Vladimir Vapnik apresentam o algoritmo SVM  (support vector machine), é um método de classificação que usa vetores de suporte para separar as classes. Resolve problemas complexos trassando hiper planos de separação 
>> - Em 1997 Deep Blue IBM vence o campeão mundial de xadrez Garry KAsparov. Ainda em 97 Jungen Schmidhuber apresenta o a LSTM(long short term memory)que permite a construção de aplicações variadas , como analise de séries temporais e reconhecimento de fala.
>> - Em 1998 o algoritimo de aprendizado de maquina mais usado no mundo é o SVM.
>> - Em 2006 o algoritimo de aprendizado de maquina mais usado no mundo é o Random Forest.
>> - Em 2012 o algoritimo de aprendizado de maquina mais usado no mundo é o Deep Learning.
>> - Em 2014 Goodfellow et all, demostra a construção de uma arquitetura para a geração de instancias a partir de duas redes neurais Redes GAN ( Generative Adversarial Networks) a partir de uma rede GAN é possivél gerar um algoritimo de deep face que converte rostos femininos em masculinos e vice versa. 


