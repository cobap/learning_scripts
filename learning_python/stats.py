#%%

from scipy.stats import norm

prob = norm.cdf(180, 170, 10) - norm.cdf(160, 170, 10)

print(prob)

#%%

prob = 1 - norm.cdf(90, 71, 15)

print(prob)

#%%

norm.rvs(1000)
