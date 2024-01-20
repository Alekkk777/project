import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
print(digits)
print(digits.DESCR)
print(digits.data)
print(digits.target)
# Figure size (width, height)

fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images

for i in range(64):

    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position

    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value

    ax.text(0, 7, str(digits.target[i]))

plt.show()
model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)
fig = plt.figure(figsize=(8, 3))

fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')
for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()
new_samples = np.array([
[0.00,0.08,2.06,3.74,3.36,0.08,0.00,0.00,0.00,2.67,7.62,7.64,7.63,4.80,0.00,0.00,0.00,0.38,2.14,0.32,3.66,7.62,2.13,0.00,0.00,0.00,0.00,0.00,0.76,7.62,3.81,0.00,0.00,0.00,0.15,2.59,6.18,7.40,1.30,0.00,0.00,1.52,7.25,7.62,7.62,6.48,4.35,0.30,0.00,1.07,5.74,6.14,6.14,6.51,6.27,0.61,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.99,5.26,3.51,1.77,0.00,0.00,0.00,0.00,3.74,7.62,7.55,7.55,4.13,0.08,0.00,0.00,3.82,7.62,0.62,5.11,7.62,4.73,0.00,0.00,3.81,7.62,0.00,0.08,4.27,7.62,2.36,0.00,3.36,7.62,1.53,0.00,0.84,7.62,3.05,0.00,0.84,7.17,7.48,6.86,7.09,7.55,1.91,0.00,0.00,1.07,4.11,4.52,4.49,2.59,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,1.07,2.82,2.97,0.38,0.00,0.00,0.00,0.00,4.96,7.62,7.62,5.95,0.08,0.00,0.00,0.00,0.23,1.17,3.14,7.62,1.98,0.00,0.00,0.00,0.00,0.00,2.75,7.62,1.76,0.00,0.00,0.00,0.99,5.57,7.55,7.32,3.81,2.21,0.00,0.00,2.97,7.62,7.62,7.62,7.64,4.73,0.00,0.00,0.38,2.85,3.09,2.62,0.23,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,2.52,4.58,3.51,0.91,0.00,0.00,0.00,1.99,7.47,7.38,7.62,7.47,4.42,0.08,0.00,5.28,7.01,0.46,1.33,4.93,7.62,4.42,0.00,7.11,4.88,0.00,0.00,0.00,5.57,6.86,0.70,7.63,4.42,0.53,0.00,2.82,7.47,5.11,0.22,6.79,7.62,7.62,7.62,7.62,5.72,0.46,0.00,0.23,2.16,3.56,3.80,3.13,0.23,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])
new_labels = model.predict(new_samples)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
print(new_labels) 