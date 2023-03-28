import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Program Files/Git/IBI1_2022-23/IBI1_2022-23/Practical7")
covid_data=pd.read_csv("full_data.csv")
# show the second column from every 100th row from the first 1000 rows.
print(covid_data.iloc[0:1001:100,2])
# show "total_cases" for all rows correspoding to Afghanisatan
print(covid_data.loc[covid_data.location=="Afghanistan","total_cases"])
# calcualte the mean number
new_data=covid_data.loc[covid_data.date=="2020-03-31",["location","new_cases","new_deaths"]]
a=new_data.iloc[:,1]
print(np.mean(a))
b=new_data.iloc[:,2]
print(np.mean(b))
# boxpolt
plt.boxplot([new_data.iloc[:,1],new_data.iloc[:,2]],labels=['new_cases','new_deaths'])
# plot the worldwide over time and the title
plt.plot(covid_data.date,covid_data.new_cases,'b+')
plt.title('world date new cases')
plt.plot(covid_data.date,covid_data.new_deaths,'b+')
plt.title('world date new deaths')
# the answers for the question
x=covid_data.loc[covid_data.location=="Germany","total_cases"]
y=covid_data.loc[covid_data.location=="Germany","total_deaths"]
print(max(y)/max(x))
m=covid_data.loc[covid_data.location=="United Kingdom","total_cases"]
n=covid_data.loc[covid_data.location=="United Kingdom","total_deaths"]
print(max(n)/max(m))
