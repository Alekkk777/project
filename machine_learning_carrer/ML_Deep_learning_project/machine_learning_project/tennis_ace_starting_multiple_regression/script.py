import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df=pd.read_csv('tennis_ace_starting_multiple_regression/tennis_stats.csv')
#print(df.head())
#print(df[['FirstServe', 'FirstServePointsWon', 'Wins', 'Winnings']].describe())

plt.scatter(df['BreakPointsOpportunities'], df['Winnings'])
plt.title('Wins vs BreakPointsOpportunities')
plt.xlabel('BreakPointsOpportunities')
plt.ylabel('Wins')
plt.show()

#analisys of scatter plot of variables to find linear regressions with winnings:
#BreakPointsOpportunities
#BreakPointsFaced
#DoubleFaults
#ReturnGamesPlayed
#ServiceGamesPlayed
#wins
#Aces

features = df[['BreakPointsOpportunities']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
model = LinearRegression()
model.fit(features_train,outcome_train)
model.score(features_test,outcome_test)
prediction = model.predict(features_test)
plt.scatter(outcome_test,prediction, alpha=0.4)


features = df[['BreakPointsOpportunities',
'FirstServeReturnPointsWon']]
outcome = df[['Winnings']]
model2 = LinearRegression()
model2.fit(features_train,outcome_train)
model2.score(features_test,outcome_test)
prediction2 = model2.predict(features_test)
plt.scatter(outcome_test,prediction2, alpha=0.4)


features = df[['BreakPointsOpportunities','BreakPointsFaced','DoubleFaults','ReturnGamesPlayed','ServiceGamesPlayed','Aces']]
outcome = df[['Winnings']]
model3 = LinearRegression()
model3.fit(features_train,outcome_train)
model3.score(features_test,outcome_test)
prediction3 = model3.predict(features_test)
plt.scatter(outcome_test,prediction3, alpha=0.4)



# perform exploratory analysis here:






















## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
