import torch
import pyro

# Seed para obter os mesmo valores que no tutorial
pyro.set_rng_seed(101)

"""
PRIMITIVE STOCHASTIC FUNCTIONS
"""
# loc = mean & scale = std deviation
loc = 0.
scale = 1.
# Criamos uma distribução normal
normal = torch.distributions.Normal(loc, scale)
# Recuperamos um sample da distribuição normal
x = normal.rsample()
# Recuperar log prob desse sensor específico:
normal.log_prob(x)

# Diferença entre r-sample e sample, é que r-sample é parametrizada por uma variável aleatória, assim, se torna derivável e pode ser utilizada
#  para construir gradientes, pois é derivável

"""
MODELO SIMPLES USANDO TORCH
"""
def weather_torch():
    cloudy = torch.distributions.Bernoulli(0.3).sample()
    cloudy = 'cloudy' if cloudy.item() == 1.0 else 'sunny'
    mean_temp = {'cloudy': 55.0, 'sunny': 75.0}[cloudy]
    scale_temp = {'cloudy': 10.0, 'sunny': 15.0}[cloudy]
    temp = torch.distributions.Normal(mean_temp, scale_temp).rsample()
    return cloudy, temp.item()

"""
MODELO SIMPLES UTILIZANDO PYRO
"""

# Pyro sample é o mesmo que chamar uma função primitiva estocástica + retorna tb uma amostra da função
x = pyro.sample('my_sample', pyro.distributions.Normal(loc, scale))
print(x)

def weather_pyro():
    cloudy = pyro.sample('cloudy', pyro.distributions.Bernoulli(0.3))
    cloudy = 'cloudy' if cloudy.item() == 1.0 else 'sunny'
    mean_temp = {'cloudy': 55.0, 'sunny': 75.0}[cloudy]
    scale_temp = {'cloudy': 10.0, 'sunny': 15.0}[cloudy]
    temp = pyro.sample('temp', pyro.distributions.Normal(mean_temp, scale_temp))
    return cloudy, temp.item()


def ice_cream_sales():
    cloudy, temp = weather_pyro()
    expected_sales = 200. if cloudy == 'sunny' and temp > 80.0 else 50.
    ice_cream = pyro.sample('ice_cream', pyro.distributions.Normal(expected_sales, 10.0))
    return ice_cream

"""
INFERENCIA COM PYRO
"""
import matplotlib.pyplot as plt
import numpy as np
import torch
import pyro
import pyro.infer
import pyro.optim
import pyro.distributions as dist

pyro.set_rng_seed(101)

# Nosso guess gera uma distribuição normal do peso. Essa distribuição normal do peso + a variação do nosso chute é a probabilidade da
# medida da pesa
def scale(guess):
    weight = pyro.sample("weight", dist.Normal(guess, 1.0))
    return pyro.sample("measurement", dist.Normal(weight, 0.75))

# Caso nosso guess seja 8.5, mas o measurement deu 9.5, como inferimos a distribuição dos dados?
# (weight | guess, measurement = 9.5) ~ ?

# Pyro condition recebe um modelo e observações, e retorna um modelo com as mesma assinaturas
conditioned_scale = pyro.condition(scale, data={"measurement": 9.5})

# Assim, podemos transformar em uma função lambda ou função normal
def deferred_conditioned_scale(measurement, guess):
    return pyro.condition(scale, data={"measurement": measurement})(guess)

# Para o conditioned scale, deferred e o scale_obs, que representam todos a mesma função. Basicamente estamos colocando os dados observados para posteriormente
# descobrimos a função probabilidade que define weight, dado que temos os dados de measurement
def scale_obs(guess):  # equivalent to conditioned_scale above
    weight = pyro.sample("weight", dist.Normal(guess, 1.))
     # here we condition on measurement == 9.5
    return pyro.sample("measurement", dist.Normal(weight, 0.75), obs=9.5)
