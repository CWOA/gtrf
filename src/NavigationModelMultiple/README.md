[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# GTRF (Grid-based Target Recovery Framework)

This repository provides a framework for rapidly prototyping, verifying and evaluating algorithmic approaches to the problem of distributed static and moving target recovery.

This repository accompanies the IROS 2018 submission entitled *"Learning to Search for Distributed Targets from UAV-like Vision"*.
All source code used to generate results and data within the submission is given here for public use, further work, replicability and transparency.

Essential dependencies
------
  * OpenCV (https://opencv.org/) - used for rendering visual input to the respective algorithm
  * Numpy (http://www.numpy.org/) - used for numerical/matrix operations
  * NetworkX (https://networkx.github.io/) - used for compute globally-optimal solutions to epsiode generations

Non-essential dependencies
------
  * TQDM (https://pypi.python.org/pypi/tqdm) - progressbar visualisation package for monitoring iterative progress in large operations (e.g. training data generation, evaluation)
  * Tensorflow v1.0+ (https://www.tensorflow.org/) - installed to support TFLearn
  * TFLearn (http://tflearn.org/) - high-level API for Tensorflow DNN operations
  * Matplotlib (https://matplotlib.org/) - used for plotting graph data
  * Scikit-learn (http://scikit-learn.org/stable/) - used for randomly segregating training towards cross-fold validation
  * ROS (http://www.ros.org/) - used to interact between main classes and Gazebo and simulate UAV-like properties
  * Gazebo (http://gazebosim.org/) - used to render simulated camera view for UAV downward vision

Overview
------


Getting started
------
Run the file "NavigationModelMultiple.py"
To add your own algorithm, edit the file "YourAlgorithm.py"

License
------
MIT License