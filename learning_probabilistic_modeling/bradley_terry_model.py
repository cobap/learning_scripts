# %% [markdown]

## The Bradley–Terry Model

# In theory, this problem should not be too hard — let them play a bunch of games and check the players win ratios. But we have 2 problems
# 

# - You cannot tell if a win ratio of close to 100 % means that the player is exceptional, or if the player only stomped weak opponents;
# - If a player only played a few games, the estimate of this player’s strength should come with high uncertainty, which a raw win ratio does not deliver.

### Model Intuition

# Players have different strengh and are rules by a equation when they compete:
# $$ P(P1 wins) = \sigma(s_1 - s_2) = exp(s_1 - s_2) / (1 + exp(s_1 - s_2)) $$

# %%

import pymc as pm
import pandas as pd
import numpy as np
np.random.seed(0)

# %%

# We create the fake dataset

def determine_winner(player_1, player_2):
    if player_1 == 0 and player_2 == 1:
        return np.random.binomial(n=1, p=0.05)
    if player_1 == 0 and player_2 == 2:
        return np.random.binomial(n=1, p=0.05)
    if player_1 == 1 and player_2 == 0:
        return np.random.binomial(n=1, p=0.9)
    if player_1 == 1 and player_2 == 2:
        return np.random.binomial(n=1, p=0.1)
    if player_1 == 2 and player_2 == 0:
        return np.random.binomial(n=1, p=0.9)
    if player_1 == 2 and player_2 == 1:
        return np.random.binomial(n=1, p=0.85)


games = pd.DataFrame({
    "Player 1": np.random.randint(0, 3, size=1000),
    "Player 2": np.random.randint(0, 3, size=1000)
}).query("`Player 1` != `Player 2`")
games["Player 1 wins"] = games.apply(
    lambda row: determine_winner(row["Player 1"], row["Player 2"]),
    axis=1
)

# %%

new_games = pd.DataFrame({
    "Player 1": [3, 3],
    "Player 2": [2, 2],
    "Player 1 wins": [1, 1]
})
games = pd.concat(
    [games, new_games],
    ignore_index=True
)

# %%

# Using PyMC3 for the modeling
# We use Gaussian priors for the players strength

with pm.Model() as model:
    strength = pm.Normal("strength", 0, 1, shape=5)
    diff = strength[games["Player 1"]] - strength[games["Player 2"]]

    obs = pm.Bernoulli(
        "wins",
        logit_p=diff,
        observed=games["Player 1 wins"]
    )

    trace = pm.sample()
