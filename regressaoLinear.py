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