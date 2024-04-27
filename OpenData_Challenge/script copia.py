import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer
from scipy.stats import yeojohnson
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
# Caricamento dei dati di training
train_data = pd.read_csv('./LWRS v2 data-set-file/train.csv', delimiter='|')

train_data.head() ,train_data.info()

# Esplorazione dei dati: visualizzazione delle distribuzioni
num_vars = ['revenues', 'pfn_ebitda', 'pn', 'ebitda']
cat_vars = ['juridical_form', 'dossier_type', 'application_source', 'credimi_industry', 'region', 'zone', 'gender']

# Visualizzazione dei dati numerici
for var in num_vars:
    plt.figure(figsize=(10, 4))
    sns.histplot(train_data[var], kde=True, bins=30)
    plt.title(f'Distribuzione di {var}')
    plt.show()

    plt.figure(figsize=(10, 4))
    sns.boxplot(x=train_data[var])
    plt.title(f'Boxplot di {var}')
    plt.show()

# Visualizzazione delle variabili categoriche
for var in cat_vars:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=train_data[var], order=train_data[var].value_counts().index)
    plt.title(f'Distribuzione di {var}')
    plt.show()

# Rimozione delle colonne non necessarie
columns_to_drop = ['sfid', 'dt_rif', 'gender', 'zone']
train_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Aggiornamento delle variabili categoriche dopo la rimozione
cat_vars = ['juridical_form', 'dossier_type', 'application_source', 'credimi_industry', 'region']
train_data[cat_vars].info()

# One-Hot Encoding delle variabili categoriche
encoder = OneHotEncoder(drop='first')
encoded_data = encoder.fit_transform(train_data[cat_vars])
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out())
train_data = pd.concat([train_data, encoded_df], axis=1)
train_data.drop(cat_vars, axis=1, inplace=True)

# Variabili numeriche di interesse
num_vars = ['revenues', 'pfn_ebitda', 'pn', 'ebitda', 'score_accounting', 'score_identity', 'score_trend']

# Imputazione dei valori mancanti per tutte le colonne numeriche
imputer = SimpleImputer(strategy='median')
train_data[num_vars] = imputer.fit_transform(train_data[num_vars])

# Applicazione della trasformazione Yeo-Johnson per correggere la distribuzione dei dati
for col in num_vars:
    train_data[col], _ = yeojohnson(train_data[col])

# Scalatura dei dati
scaler = RobustScaler()
train_data[num_vars] = scaler.fit_transform(train_data[num_vars])

# Stampa dei primi dati per conferma
print(train_data.head())
# Addestramento del modello
X_train = train_data.drop('target', axis=1)
y_train = train_data['target']
model = SVC(kernel='linear')
model.fit(X_train, y_train)
# Caricamento e preparazione del dataset di test
test_data = pd.read_csv('./LWRS v2 data-set-file/test.csv', delimiter='|')
test_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
encoded_test_data = encoder.transform(test_data[cat_vars])
encoded_test_df = pd.DataFrame(encoded_test_data.toarray(), columns=encoder.get_feature_names_out())
test_data = pd.concat([test_data, encoded_test_df], axis=1)
test_data.drop(cat_vars, axis=1, inplace=True)
test_data[num_vars] = imputer.transform(test_data[num_vars])
for col in num_vars:
    test_data[col], _ = yeojohnson(test_data[col])
test_data[num_vars] = scaler.transform(test_data[num_vars])

# Predizione sul dataset di test
X_test = test_data.drop('target', axis=1, errors='ignore')  # Se target non esiste
predictions = model.predict(X_test)

test_data_load = pd.read_csv('./LWRS v2 data-set-file/test.csv', delimiter='|')
# Salvataggio delle previsioni in un file CSV
output = pd.DataFrame({'ID': test_data_load['sfid'], 'Prediction': predictions})
output.to_csv('predictions.csv', index=False)

print("Predizioni salvate nel file 'predictions.csv'.")