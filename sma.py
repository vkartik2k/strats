import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import math

df = pd.read_csv('dataset/NESTLEIND.NS.csv')

arr = df.values

date = []
closing_price = []

for i in arr:
    if i[-2] and not math.isnan(i[-2]):
        date.append(i[0])
        closing_price.append(i[-2])

n = len(date)

SMA20 = []
SMA50 = []
SMA200 = []

total20 = 0

for i in range(19):
    SMA20.append(-1)
    total20 += closing_price[i]

for i in range(19, n):
    total20 += closing_price[i]
    SMA20.append(total20/20)
    total20 -= closing_price[i-19]

total50 = 0

for i in range(49):
    SMA50.append(-1)
    total50 += closing_price[i]

for i in range(49, n):
    total50 += closing_price[i]
    SMA50.append(total50/50)
    total50 -= closing_price[i-49]

total200 = 0

for i in range(199):
    SMA200.append(-1)
    total200 += closing_price[i]

for i in range(199, n):
    total200 += closing_price[i]
    SMA200.append(total200/200)
    # print(SMA200[-1],i)
    total200 -= closing_price[i-199]

# plt.title("Line graph")  
# plt.xlabel("X axis")  
# plt.ylabel("Y axis") 
# plt.plot(date, SMA200, color ="black")  
# plt.plot(date, SMA50, color ="red")  
# plt.plot(date, SMA20, color ="green")  
# plt.plot(date, closing_price, color ="blue")  
# plt.show()




# Trading Strategy - SMAs

holding = False
buyingPrice = 0
buyingDate = ""

trades = []


for i in range(n) :
    if not holding :
        if SMA200[i] > SMA50[i] and SMA50[i] > SMA20[i] and SMA20[i] > closing_price[i] :
            holding = True
            buyingPrice = closing_price[i]
            buyingDate = date[i]
    else :
        if SMA200[i] < SMA50[i] and SMA50[i] < SMA20[i] and SMA20[i] < closing_price[i] :
            holding = False
            trades.append([((closing_price[i]-buyingPrice)/buyingPrice), buyingDate, date[i]])
            print("Percentage Gain:", trades[-1][0], "       Buying Date:", trades[-1][1], "      Selling Date:", trades[-1][2])




