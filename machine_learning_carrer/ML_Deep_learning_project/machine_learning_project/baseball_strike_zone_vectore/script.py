import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from players import aaron_judge, jose_altuve, david_ortiz
import numpy as np

def draw_boundary(ax, classifier):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Crea una griglia da visualizzare
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 30),
                         np.linspace(ylim[0], ylim[1], 30))
    
    # Calcola i valori Z per la griglia usando il classificatore
    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Disegna il confine decisionale
    ax.contour(xx, yy, Z, colors='k', levels=[0], alpha=0.5,
               linestyles=['-'])

# Il resto del tuo codice rimane invariato
fig, ax = plt.subplots()
print(aaron_judge.description.unique())
print(aaron_judge.type.unique())
aaron_judge.type = aaron_judge.type.map({'S':1, 'B':0})
print(aaron_judge['plate_x'])
aaron_judge = aaron_judge.dropna(subset = ['type', 'plate_x', 'plate_z'])
plt.scatter(x = aaron_judge.plate_x, y = aaron_judge.plate_z, c = aaron_judge.type, cmap = plt.cm.coolwarm, alpha = 0.25)

training_set, validation_set = train_test_split(aaron_judge, random_state = 1)
classifier = SVC(kernel = 'rbf', gamma = 3, C = 1)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

ax.set_ylim(-2, 2)
draw_boundary(ax, classifier)
plt.show()

print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type']))
