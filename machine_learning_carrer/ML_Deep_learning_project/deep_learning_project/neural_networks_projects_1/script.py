import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.optimizers import Adam

# Carica il dataset
dataset = pd.read_csv('life_expectancy.csv')

# Visualizza il dataset
print(dataset.head())
print(dataset.describe())

# Rimuovi la colonna 'Country'
dataset = dataset.drop(['Country'], axis=1)

# Dividi il dataset in etichette e caratteristiche
labels = dataset.iloc[:, -1]
features = dataset.iloc[:, 0:-1]

# Pre-elaborazione dei dati: Converti le variabili categoriche in dummy/indicatori
features = pd.get_dummies(features)

# Divisione in set di addestramento e test
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20, random_state=23)

# Inizializza e applica ColumnTransformer per la normalizzazione
ct = ColumnTransformer([("numeric", StandardScaler(), features.columns)])

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

# Costruzione del modello
my_model = Sequential()
my_model.add(InputLayer(input_shape=(features.shape[1],)))

# Aggiungi un solo livello nascosto
my_model.add(Dense(64, activation='relu'))  # Puoi cambiare il numero 64 con qualsiasi altro numero di unità

# Aggiungi il livello di output per la regressione
my_model.add(Dense(1))  # 1 nodo per la regressione

print(my_model.summary())

#Optimizer
opt = Adam(learning_rate = 0.01)
#Compiliamo
my_model.compile(optimizer=opt, loss='mse', metrics=['mae'])

# Addestra il modello
my_model.fit(features_train_scaled, labels_train, epochs=50, batch_size=1, verbose=1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose = 0)

print(res_mse,res_mae)
#vediamo che mae= circa 2 che è un errore accettabile su 70 anni di vita media 