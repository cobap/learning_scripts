# %%

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import seaborn as sns
# import sklearn

# %%

# We define all possible states
customer_state = ['Ordering the coffee','Waiting for your coffee','Leaving']
states = {'O':customer_state[0],'M':customer_state[1],'L':customer_state[2]}

# %%

mu, sigma = 5, 1

def one_drink_one_cust():
    start = states['O']
    print(start+'\n')
    ordering_time = 0.5
    first_state = states['M']
    print(first_state+'\n')
    waiting_time = 0
    k = 0
    while k == 0:

        # Get likelihood of waiting time
        p = scipy.stats.norm.cdf(waiting_time, loc=mu, scale=sigma)

        # Check by random choice if coffee is ready indeed
        k = np.random.choice([0, 1], p=[1-p, p])
        waiting_time = waiting_time+0.5
        
        if k == 0:
            print('Coffee is brewing... \n')
    
    print('Your coffee is ready! \n')
    print(states['L']+'\n')
    print('Waiting time is = %.2f' % (waiting_time))
    return waiting_time

# %%


kind_of_coffee = np.array(pd.read_csv('./dados/starbucks-menu-nutrition-drinks.csv')['Unnamed: 0'])

# We define as a range between 50/100 for each drink in startbucks
p_start = [np.random.choice(np.arange(50, 100)) for _ in range(len(kind_of_coffee))]

# Probability of each drink
p_start = np.array(np.array(list(np.array(p_start)/sum(p_start))))

# %%

coffee_data = pd.DataFrame(kind_of_coffee, columns=['State 1'])
mu_list = []
var_list = []
for i in range(len(coffee_data)):
    mu_list.append(np.random.choice(np.linspace(3, 6, 1000)))
    var_list.append(np.random.choice(np.linspace(0.1, 1.5, 1000)))
coffee_data[r'$\mu$'] = mu_list
coffee_data[r'$\sigma$'] = var_list
coffee_data[r'$p$'] = p_start
coffee_data.head()

# %%


def random_drink_one_cust():
    start = states['O']
    # print(start+'\n')
    ordering_time = 0.5
    first_state = states['M']
    chosen_i = np.random.choice(range(0, len(kind_of_coffee)), p=p_start)
    # print('Ordering coffee %s' % (kind_of_coffee[chosen_i]))
    # print(first_state+'\n')

    mu_i, var_i = coffee_data[r'$\mu$'].loc[chosen_i], coffee_data[r'$\sigma$'].loc[chosen_i]
    waiting_time = 0
    k = 0
    while k == 0:
        p = scipy.stats.norm.cdf(waiting_time, loc=mu_i, scale=var_i)
        k = np.random.choice([0, 1], p=[1-p, p])
        waiting_time = waiting_time+0.5
        if k == 0:
            print('Coffee is brewing... \n')
    # print('Your coffee is ready! \n')
    # print(states['L']+'\n')
    # print('Waiting time is = %.2f' % (waiting_time))
    return waiting_time


random_drink_one_cust()

# %%

waiting_time_list = []
for i in range(10000):
    waiting_time_list.append(random_drink_one_cust())
plt.figure(figsize=(20,10))
plt.subplot(2,1,1)
sns.histplot(waiting_time_list,fill=True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Waiting time (minutes)',fontsize=14)
plt.ylabel('Count',fontsize=14)
plt.subplot(2,1,2)
sns.kdeplot(waiting_time_list,fill=True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Waiting time (minutes)',fontsize=14)
plt.ylabel('Probability Density Function (PDF)',fontsize=14)