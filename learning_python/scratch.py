import requests

url = 'https://api.telegram.org/bot1158500189:AAFJUrrqMIy2h3YCfhELCNWkyKVCCDXIeoY/sendMessage?chat_id=@labaulasleads&text=Novo pedido de aula recebido. Detalhes abaixo:'













import matplotlib.pyplot as plt
import math

x = [1,2,3,4]
y = [30,50,60,70]
plt.plot(x, y)

x2 = [1,2,3,4]
y2 = [30 * math.log(x) + 30 for x in x2]
plt.plot(x2, y2)

valor_aula = lambda x, y: (28 * math.log(y) + 30) + (30 * math.log(y) + 30)*x

# x = numero alunos
# y = horas/aula
valor_aula(1,1)
valor_aula(1,2)
valor_aula(2,1)
valor_aula(3,3)
valor_aula(3,4)
valor_aula(4,4)
