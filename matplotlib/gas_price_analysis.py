import sys
print(sys.path)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
gas=pd.read_csv('gas_prices.csv')
# gas.columns = ["Year","Australia","Canada","France","Germany","Italy","Japan","Mexico","South Korea","UK","USA"]
# gas=pd.read_excel('gas_prices.xlsx')
# print(gas)
# print(gas.Year)
# data.columns = data.columns.str.strip()
# print(data.columns)
# plt.figure(figsize=(20,10))
# plt.plot(gas.Year, gas.France,label='FRA Gas Prices', marker='.', linestyle='--')
# plt.plot(gas.Year, gas.Canada,label='CAN Gas Prices', marker='.', linestyle='--')
# plt.plot(gas.Year, gas['USA'],label='USA Gas Prices', marker='.', linestyle='--')
list_of_countries=['Australia', 'USA', 'Canada']
l=[]
for ele in gas:
    # if ele in list_of_countries:
    if ele != 'Year':
        l.append(ele)
        plt.plot(gas.Year, gas[ele], marker='.', linestyle='--')
        plt.legend(l)
plt.title('Evolution of gas prices from 1990 to 2008 in dollars/liter in several countries')
plt.xlabel("years", fontdict={'fontname':'Comic Sans MS'})
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.ylabel('prices $/Liter', fontdict={'fontname':'Comic Sans MS'})

# plt.savefig("gas_price_evolution_FRA&CAN&USA.png")
plt.savefig("gas_price_evolution.png")
plt.show()
plt.draw()