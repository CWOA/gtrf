#!/usr/bin/env python

import DNN
import Constants as const
from FieldMap import FieldMap

"""
This class forms the principal entry point for selecting experimentation,
see the main function below
"""

# Generate training data, save it to file and use as training data for DNN training
# then evaluate on the best model yielded from cross-fold validation
def generateTrainTest(experiment_name, iterations, visualise, use_simulator):
	# Experiment parameters
	# experiment_name = "individual_motion_10k"
	# experiment_name = "visitation_marked_TO"

	# Initialise FieldMap instance for training data generation and perform it
	train_fm = FieldMap(	True, 
							experiment_name, 
							visualise=visualise, 
							use_simulator=use_simulator, 
							save=True						)
	saved_to_path = train_fm.generateTrainingData(iterations)

	# Can comment the above two lines and uncomment the one below to just run data
	# generation and testing
	# saved_to_path = "/home/will/catkin_ws/src/uav_id/tflearn/ICIP2018/data/TRAINING_DATA_visitation_marked_TO.h5"
	# saved_to_path = "/home/will/catkin_ws/src/uav_id/tflearn/ICIP2018/data/TRAINING_DATA_individual_motion_20k.h5"

	# Use this training data to initialise and train the dual input CNN
	dnn = DNN.DNNModel(use_simulator=use_simulator)
	best_model_path = dnn.trainModel(experiment_name, data_dir=saved_to_path)

	# best_model_path = "/home/will/catkin_ws/src/uav_id/tflearn/ICIP2018/models/visitation_marked_TO_2018-02-13_22:28:27_CROSS_VALIDATE_4.tflearn"
	# best_model_path = "/home/will/catkin_ws/src/uav_id/tflearn/ICIP2018/models/individual_motion_60k_2018-02-16_10:29:15_CROSS_VALIDATE_0.tflearn"

	# Use the best model path to test
	# test_fm = FieldMap(		False, 
	# 						experiment_name, 
	# 						visualise=visualise, 
	# 						use_simulator=use_simulator, 
	# 						model_path=best_model_path		)
	# test_fm.startTestingEpisodes(iterations)

# Just generate training examples
def generateTrainingExamples(iterations, visualise, use_simulator, save_video):
	# Experiment parameters
	experiment_name = "video_test"

	fm = FieldMap(	True,
					experiment_name,
					visualise=visualise, 
					use_simulator=use_simulator, 
					save=True, 
					save_video=save_video 			)
	fm.generateTrainingData(iterations)

"""
Train model on synthesised data
DON'T EXECUTE VIA ROSLAUNCH (no need to do so, just launch via python/terminal)
"""
def trainModel(iterations, use_simulator):
	pass

# Testing trained model on real example/problem
def testModel(iterations, visualise, use_simulator):
	# Experiment parameters
	experiment_name = "motion_test_MS"

	fm = FieldMap(False, experiment_name, visualise=visualise, use_simulator=use_simulator)
	fm.startTestingEpisodes(iterations)

# Method for testing/comparing solver methods
def compareSolvers(iterations, visualise):
	fm = FieldMap(True, visualise=visualise, use_simulator=False, second_solver=True)
	fm.compareSolvers(iterations)

# Entry method
if __name__ == '__main__':
	"""
	Function calls

	Constant arguments to functions can be overidden here, by default run-time
	arguments are located at the top of the "Constants.py" file
	"""

	# Whether to visualise visual input/map via OpenCV imshow for debugging purposes
	visualise = const.VISUALISE

	# Whether or not to use ROS/Gazebo simulator for synthesised visual input
	use_simulator = const.USE_SIMULATOR

	# Number of episodes to test on or generate training examples
	iterations = const.ITERATIONS

	# Save frames to individual per-episode videos?
	save_video = const.SAVE_VIDEO

	"""
	Primary function calls
	"""

	generateTrainTest("individual_motion_10k", 10000, visualise, use_simulator)
	const.ITERATIONS = 5000
	generateTrainTest("individual_motion_5k", 5000, visualise, use_simulator)
	# generateTrainingExamples(iterations, visualise, use_simulator, save_video)
	# trainModel(iterations, use_simulator)
	# testModel(iterations, visualise, use_simulator)
	# compareSolvers(iterations, visualise)
