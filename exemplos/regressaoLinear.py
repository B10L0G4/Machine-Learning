import numpy as np
from sklearn.linear_model import LinearRegression

# treinar um modelo de regressão é estimar os valores de coeficientes a e b que melhor vão descrever os dados 

reg = LinearRegression()
reg.fit(x,y)

#coeficienres de a e b estimados pelo modelo 
print('a estimadi', reg.coef.ravel()[0])
print('b estimado', reg.intercept_[0])

#score do modelo delimita o quão bem o modelo se ajusta aos dados , quando mais próximo de 1 melhor e quandto mais proximo de 0 pior 

print('score', reg.score(x,y))

#predict é usado para fazer previsões com o modelo treinado 

print('previsão', reg.predict(np.array([[5]])))

#r2 score é uma medida de quão bem o modelo se ajusta aos dados , quando mais proximo de 1 melhor é e quanto mais proximo de 0 pior é , o modelo r2 é uma forma de avaliar o modelo de regrassão e é calculado da sehuinte forma: 
#r2 = 1 - (SSres/SStot)
#onde SSres é a soma dos quadrados dos residuos e SSTat é a soma dos quadrados totais. 