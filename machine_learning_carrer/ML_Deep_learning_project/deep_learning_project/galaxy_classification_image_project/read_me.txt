In this project, we will build a neural network to classify deep-space galaxies. We will be using image data curated by Galaxy Zoo, a crowd-sourced project devoted to annotating galaxies in support of scientific discovery.

We will identify “odd” properties of galaxies. The data falls into four classes:

[1,0,0,0] - Galaxies with no identifying characteristics.
Three regular galaxies. Each has a bright center, surrounded by a cloud of stars.

[0,1,0,0] - Galaxies with rings.
Three ringed galaxies. Each has a bright center, surrounded by a ring of stars.

[0,0,1,0] - Galactic mergers.
Three photos of galaxies. Each contains two bright orbs surrounded by clouds. These images show galaxies in the process of merging.

[0,0,0,1] - “Other,” Irregular celestial bodies.