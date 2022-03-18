# Reinforcement Learning

- Markov decision process
- Bellman equations
- Dynamic programming
- Monte Carlo methods
- Temporal difference learning


## Como?

Não existem variáveis target, apenas sinais positivos e negativos, e uma função para otimizarmos

## Características

- Sem variáveis IID
- Tempo é crucial, decisões sequenciais que alcançam um objetivo
- O feedback sobre uma ação pode não ser instantâneo
- O agente recebe feedback sobre suas ações

## Básico

- Ambiente
- Agente
- Estado
- Objetivo
- Ação
- Protocolo (Policy) - ação que precisa ser executada pelo agente em algum estado do ambiente. É o mapa entre estado e ação. Pode ser determinístico ou estocástico
- Melhor Protocolo - É o protocolo gerado no treinamento, define o Q-learning e é sempre melhorada.
- Recompensa
- Função valor - é a predição da recompensa futura de cada estado. É usado para avaliar quais estados são bons ou ruins. O que altera a ação do agente
- Episódio/Trials - número de passos necessários para alcançar o objetivo
- Horizonte - número de passos futuros que o algoritmo vê para maximizar a recompensa. O horizonte pode ser infinito, mas ai é descontado para que o algoritmo possa converger
- Exploration vs Exploitation - são 2 lados de uma mesma moeda. Se o algoritmo explorar demais, arrisca de menos. Se arriscar demais, explora de menos.
- Função valor-estado vs valor-ação - 

