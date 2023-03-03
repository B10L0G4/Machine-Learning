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

- **o q é um algoritmo de aprendizado de maquina ? ele melhora o desempenho para uma melhor experiencia ( fica cada vez mais proximo do resulktado correto)**

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

> ### O que buscamos quando com uma aplicação de ML?
> Resolver uam tarefa com a melhor assertividade possivél.
> O modelo deve ser capaz de se adaptar a novos dados 
>O modelo deve ser capaz de generalizar a partir dos dados de treinamento. (treinar um modelo é ajusatar os parametros do modelo para que ele se adeque aos dados de treinamento.)

# Entendimento do Problema
> - Entender o problema é uma das partes essenciais para o sucesso de um projeto. 
> - A avaliação do probelma nós dá a visão de qual tipo de algoritmo utilizar. 

### O que é dimensionamento ? 
>  - Dimensionalidade representa as dimensões espacial dos dados.  Podemos trabalhar em dimensões de 1 a 3 ( 1- linha, 2 - plano(x,y), 3 -cubo (x,y,z)).Um espaço multimensional não são vários datasets(conjunto de dados) , e sim um conjunto de dados com várias dimensões. 
>  - Cada dimensão perpendicular a outras.
>  - no dataset as colunas representam as caracteristicas e as instancias são as linhas. 
>  - O numero de colunas pode ser a repsentatividade das dimensões.  


### Linear e não linear 
>  - Um modelo linear é um modelo que pode ser representado por uma equação linear.
>  - Um modelo não linear é um modelo que não pode ser representado por uma equação linear.

### Transformação
>  - È um forma de transforma os dados de entrada em uma forma que o modelo seja trasformado em uma forma linear e deixar o modelo mais simples. 

### Passos para escolha de modelos 
>  - 0 - Conhecer o Problema (analisar o problema)
>> - a partie a analise do problema , identificaremos o modelo "ideal" para a resolução da tarefa , restrições,caracteristicas, tipos de dados a serem coletados.  
>  - 1 - Coleta de daods - procurar as fontes de dados para resolver a tarefa 
>  - 2 - Prearação dos dados, adequar o formato dos dados para o modelo. (limpesa dos dados)
>  - 3 - Escolha do modelo - treinar o modelo com o dados preparados.  
>  - 4 - avaliação e sintonia de parametros - analisar o resultado do modelo e ajustar os parametros para melhorar o resultado. 
>  - 5 - Deploy - colocar o modelo em produção. 

### BIG DATA 
>  - O que ´Big Data ? 
>  É um termo utilizado para um conjunto de dados muito grande e complexo, tormado o armazenamento e processamento  através das ferramentas tradicionais.  
>  - os V's do Big Data 
>> - **Volume** - quantidade de dados 
>> - **Velocidade** - velocidade de processamento - processamento em tempo real.
>> - **Variedade** - tipos de dados - estruturados(tabelas com linhas e colunas ), semi-estruturados(necessitam de alguma transformação de dados (JSON, XML e outros)) e não estruturados(musicas, videos, logs e outros).
>> - **Veracidade** - qualidade dos dados - dados faltantes, dados duplicados, dados inconsistentes, dados incorretos. 
>> - **Valor** - utilidade dos dados - dados que podem ser utilizados para tomada de decisão.
>

### FrameWorks de desenvolvimento
>  - **Anacaonda** - é um ambiente de desenvolvimento integrado (IDE) para a linguagem de programação Python e R. 
>  - **Kaggle** - é uma plataforma de ciência de dados e aprendizado de máquina que permite que os usuários compartilhem dados, códigos e análises.
>  - **Spark** - é um framework de processamento de dados em cluster, que permite a execução de aplicações em paralelo em um cluster de computadores.
>  - **databricks** - é uma plataforma de computação em nuvem que permite a execução de aplicações em cluster de computadores.
>  - **Azure Machine Learning** - permite a criação de modelos.(pago)
>  - **AWS Machine Learning** - é uma plataforma de computação em nuvem que permite a execução de aplicações em cluster de computadores.(pago)
>  - **H2O** - ferramenta de aprendizado de máquina de código aberto que permite a execução de aplicações em cluster de computadores.

### Tarefas de Aprendizado de Máquina 
> Quais problemas resolver e como podemos selecionar os algoritmos ou classe de algoritmos
>  - Classificação 
>  - O que é classficação ? 
>> - muito utilizado, realiza o mapeamento de um conjunto de entrada e um numero finito de saidas ( temos quantidades definidas de saidas).
>> - 
>  - Tipos de Classificação 
>>  - Classificação binaria : temos duas classes possiveis de saida (0 ou 1, sim ou não, verdadeiro ou falso, positivo ou negativo, etc).   
>>  -  Algoritmos mais utilizados : Regressão Logistica, Suporte Vector Machines, Arvores de decisão, Naive Bayes , KNN 
>
>  - Classificação multiclasse : possui várias opções de saida, não exite uma classe normal ou não normal. 
>> - Algoritmos mais utilizados : Regressão Logistica, Suporte Vector Machines, Arvores de decisão, Naive Bayes , KNN, Random Forest, Gradiente Boosting, Redes Neurais artificiais.
>
>  - Multi-Labels :   temos uma entrada e várias classes distintas ou seja uma entrada pode pertencer a mais de uma classe. 
>> - Algoritmos mais utilizados : Multi-Label Arvore de decisão , Multi-Label Ramdom Forest, Multi Label Gradiente Boosting.
> 
>  - Desbalanceada : quando uma classe possui muitas instancias em releção a outra.
>> - Algoritmos mais utilizados : Estatisticas de Amostragem - Random UnderSampling, Smote OverSampling, Cost-Logist Regression ,Cost-Support Vector Machine, Cost- Arvore de Decisao, Estatisticas de avaliação - Precision Recal F1-Score, Matris de Confusão Curva ROC. 
>
>  - 

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




### Reconhecimento de Padrões  
>  - O que é reconhecer padrões ? 
>> é uma tarefa de aprendizado de maquina que tem como objetivo identificar padrões em dados. 
>  - Reconhecimento de padrões - reconhece de maneira rapida e precisa, recenhecer padrões não familiares, reconhecer formas e objetos de diferentes angulos e tamanhos, identificar objetos mesmo que sobrepostos.  
>  - onde encontramos, visão computacional, identificação de objetos, speech recognition, analise de sinais.  

### Sistemas de Recomendação 
>
>  - O que é um sistema de recomendação ?
>> - é um sistema que identifica padrões de similaridas entre itens e recomenda itens similares a um usuario. É responsavél por recomendar produtos, filmes, musicas, etc, com caracteristicas similares. 
>  - tipos de sistemas de recomensação : Baseada no usuario - recomenda itens que outros usuarios com perfis similares gostaram. Baseada em conteudo - recomenda itens que tem caracteristicas similares aos itens que o usuario gostou. Baseada em modelo - recomenda itens que tem caracteristicas similares aos itens que o usuario gostou. 

### Processamento de Linguagem Natural - NLP 
>  - O que é NLP ?
>> - e uma area da IA que estuda a interação entre computadores e linguagem humana. 
>> - O objetivo é criar sistemas que possam entender e gerar linguagem humana. A base da PLN é a transformação da base de conhecimento em dados computacionais (numericos)
> - Chatbots - são sistemas que simulam conversas com humanos. 
> - Reconhecimento de voz - é a capacidade de uma sistema de computador de reconhecer e interpretar falas humanas. 


### Analise de Sentimento
> - O que é analise de sentimento ?
>> - é a tarefa de identificar e extrair opiniões, sentimentos e emoções expressões em textos ou seja analisar os sentimentos dos usuarios a partir de textos e avaliações. 
>  - Desenvolvimento de aplicações - 
>> - Devemos retirar, emoticons, extensoes de arquivos, links, www e  etc. Normalização de textos, deixar todos os caracteres em caixa 
baixa por eexemplo
>> Tokenização de palavras dividir o texto em palavras 
remoção de stopwordsd, são palavras que dão pouco ou nenhum significado ao texto
>> Stemização / lematização , são palavras que possuim mesmo sentido nas escritas de diferentes formas. ( na lematização temos a necessidade de ter a palavra no final da lematização ( gatos, gatinhas = gato) , já no Stening iremos pegar a raiz da palavra (gato = gat) )
>> Tranformação dos textos em vetores : é o processo de transformar o texto em vetor numerico.
> - Bag of works - é um modelo de representação de textos que descreve a ocorrencia de Palavras em um texto. Textos são trnsformados em, palavras e a frequencia de cada palavra é contado. 
> - word to vec  - é um modelo que mantem o modelo de contexto das palavras. Mantem o conceito de vetor e agrupa palavras que possuem o mesmo significado/similaridade.Assim é possuvél fazer operações com as palavras eobter resultados semanticos. 
> -  Aplicação Conceitual : após o pré processamente dos dados, podemos aplicar algoritmos de classificação para classificar os textos em positivos ou negativos. 

### Series Temporais
>
> - O que é uma serie temporal ? 
>> - é uma sequencia de valores que possuem uma certa dependencia. 
>> - autocorrelação - é a correlação entre os valores dentro de uma série temporal, ou seja a correlção vem de dentro da série temporal ( valor atual com valor passado )
> - Serie Estacionaria : é uma série temporal que não apresenta tendência ou sazonalidade, a estrutura varia com o tempo. 
> - Tendecia : é uma tendencia de crescimento ou descrecimento da serie temporal. 
> - variancia constante - a variancia da serie temporal é constante ao longo do tempo.  


### Visão Computacional 
> 
> - O que é visão computacional ?
>> é a capacidade de um computador de entender e processar imagens como se fossem humanos. Corresponde a analise, compreensão e interpretação de imagens. 
> - Todos esses processos devem ocorrer de forma automatica, sem a necessidade de intervenção humana. 
> - Classificação de imagens - é a tarefa de classificar imagens em categorias.
> - Classificação + localização : é a tarefa de identificar e localizar objetos em imagens.
> - Detecção de objetos - é a tarefa de identificar objetos em imagens, a partir de uma imagem com mais de um objeto.
> - Segmentação de imagens - é a tarefa de dividir uma imagem em regiões de interesse, identifica a partir dos contornos das imagens.
> - Reconhecimento facial - é a tarefa de identificar uma pessoa em uma imagem.
> - Algoritmos utilizados : Algoritmos utilizados, redes neurais convcionais. 
> - YOLO - é um algoritmo de detecção de objeto que é capaz de detectar objetos em imagens e videos em tempo real. Utiliza apneas uma rede neural. 

### Conceitos de aulas - 02/03
> - Fundamentos
>> - 


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


