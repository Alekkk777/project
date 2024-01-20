from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

# Dati per porte logiche
data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels_and = np.array([0, 0, 0, 1])  # Uscite per AND
labels_or = np.array([0, 1, 1, 1])   # Uscite per OR

# Impostazioni per il plot
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

# Addestra Perceptron per AND
classifier_and = Perceptron(max_iter=40, random_state=22)
classifier_and.fit(data, labels_and)

# Calcola i confini decisionali per AND
distances_and = classifier_and.decision_function(point_grid)
distances_matrix_and = np.reshape(distances_and, (100, 100))

# Addestra Perceptron per OR
classifier_or = Perceptron(max_iter=40, random_state=22)
classifier_or.fit(data, labels_or)

# Calcola i confini decisionali per OR
distances_or = classifier_or.decision_function(point_grid)
distances_matrix_or = np.reshape(distances_or, (100, 100))

# Plot per AND
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1 riga, 2 colonne, posizione 1
plt.title('Perceptron per AND')
plt.scatter(data[:, 0], data[:, 1], c=labels_and)
heatmap_and = plt.pcolormesh(x_values, y_values, distances_matrix_and, shading='auto')
plt.colorbar(heatmap_and)
plt.xlabel('X1')
plt.ylabel('X2')

# Plot per OR
plt.subplot(1, 2, 2)  # 1 riga, 2 colonne, posizione 2
plt.title('Perceptron per OR')
plt.scatter(data[:, 0], data[:, 1], c=labels_or)
heatmap_or = plt.pcolormesh(x_values, y_values, distances_matrix_or, shading='auto')
plt.colorbar(heatmap_or)
plt.xlabel('X1')
plt.ylabel('X2')

plt.tight_layout()
plt.show()

