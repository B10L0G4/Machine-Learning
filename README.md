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


> Normalização de dados - é o processo de transformar os dados em uma escala comum, sem distorcer as diferenças no intervalo de valores. 
> Quando normalizar meus dados : sempre que os dados estiverem em escalas diferentes, as vanatagens : são que os dados são normalizados e os algoritimos de aprendizado convergem mais rapidamente.
>  

### FrameWorks de desenvolvimento
>  - **Anacaonda** - é um ambiente de desenvolvimento integrado (IDE) para a linguagem de programação Python e R. 
>  - **Kaggle** - é uma plataforma de ciência de dados e aprendizado de máquina que permite que os usuários compartilhem dados, códigos e análises.
>  - **Spark** - é um framework de processamento de dados em cluster, que permite a execução de aplicações em paralelo em um cluster de computadores.
>  - **databricks** - é uma plataforma de computação em nuvem que permite a execução de aplicações em cluster de computadores.
>  - **Azure Machine Learning** - permite a criação de modelos.(pago)
>  - **AWS Machine Learning** - é uma plataforma de computação em nuvem que permite a execução de aplicações em cluster de computadores.(pago)
>  - **H2O** - ferramenta de aprendizado de máquina de código aberto que permite a execução de aplicações em cluster de computadores.


### Naive Bayes 
> - é um algoritmo de aprendizado de máquina baseado no teorema de Bayes com uma suposição de independência entre os preditores.
> - 

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



## **História** 

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

>> 
