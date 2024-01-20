import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("codecademyproject/python_project_codecademy/machine_learning_project/honey_production_linear_regression/db_honey.csv")
#see the structure od db
#print(df.head())
#we want to get the total production of honey per year(first column with year and second with average)
prod_per_year=df.groupby('year').totalprod.mean().reset_index()
#we want to store year in a variable(we have to reshape)
X=prod_per_year["year"]
X = X.values.reshape(-1, 1)
#now we store the total prod
y=prod_per_year["totalprod"]
plt.scatter(X,y)
plt.show()
#create our model
regr=linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_[0])
print(regr.intercept_ )
y_predict=regr.predict(X)
#let's plot
plt.plot(X,y_predict)
#the production is in decline so we want to have a preview of what will happen
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)
future_predict=regr.predict(X_future)
plt.plot(X_future,future_predict)
plt.show()
