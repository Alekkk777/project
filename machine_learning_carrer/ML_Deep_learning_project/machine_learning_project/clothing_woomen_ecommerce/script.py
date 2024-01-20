import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
#import data
df = pd.read_csv('codecademyproject/python_project_codecademy/machine_learning_project/clothing_woomen_ecommerce/Womens Clothing E-Commerce Reviews.csv')
#print column names and info
print(df.columns)
print(df.info())

#print the count of the recommended features 
print(df['recommended'].value_counts())
#is true/false function e we want to transform to a numerical 0/1 function so we create a binary dictionary
binary_dict = {True:1, False:0}
#create a new column
df['recommended'] = df['recommended'].map(binary_dict)
#print your transformed column
print(df['recommended'].value_counts())

#let's do a similar things with rating feature
print(df['rating'].value_counts())
#we have ordinal text data so w want to transform in numerical data
rating_dict={'Loved it':5,'Liked it':4,'Was okay':3,'Not great':2,'Hated it':1,}
#using dictionary to convert data
df['rating'] = df['rating'].map(rating_dict)

#same things with department_name
print(df['department_name'].value_counts())
#we decide to use one-hot encode
# use pandas .get_dummies method to create one new column for each color
ohe = pd.get_dummies(df['department_name'])

# join the new columns back onto our cars dataframe
df = df.join(ohe)
#let's print
print(df.columns)

#same with review_date, it was an object and we want to transform into a data/time feature
df['review_date'] = pd.to_datetime(df['review_date'])
print(df['review_date'].dtypes)

#now we want to scaling our data-> we put everything on the same scale
df_1 = df[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()
#reset index
df_1 = df_1.set_index(df_1['clothing_id'])
#scale our data
scaler = StandardScaler()
scaler.fit_transform(df_1)