#!/usr/bin/env python

from Utility import Utility
import random
import Constants as const

class Object:
	# Class constructor
	def __init__(	self, 
					is_agent, 
					x=const.AGENT_START_COORDS[0], 
					y=const.AGENT_START_COORDS[1]	):
		### Class attributes/properties

		# Am I the agent or a target?
		self._agent = is_agent

		# Object position (x, y) coordinates
		self._x = x 
		self._y = y

		# Variables depending on whetherh we're the agent
		if self._agent:
			# Colour to render for visualisation
			self._colour = const.AGENT_COLOUR
		else:
			# As a target, have we been visited before
			self._visited = False

			# Colour to render for visualisation
			self._colour = const.TARGET_COLOUR

	def getVisited(self):
		return self._visited

	def setVisited(self, visited):
		self._visited = visited

	def getPos(self):
		return self._x, self._y

	def getPosTuple(self):
		return (self._x, self._y)

	def setPos(self, x, y):
		if self._agent:
			self._x = x
			self._y = y
		else:
			Utility.die("Trying to directly set position of non-agent")
		
	def getColour(self):
		return self._colour

class ObjectHandler:
	# Class constructor
	def __init__(	self,
					random_agent_pos=True,
					random_num_targets=False	):
		"""
		Class arguments from init
		"""

		# Should the agent's position be randomised or some default position
		self._random_agent_pos = random_agent_pos

		# Should we randomise the number of targets or not
		self._random_num_targets = random_num_targets

		"""
		Class attributes
		"""

		self._agent = None
		self._targets = None

		print "Initialised ObjectHandler"

	# Reset this handler so we can go again
	def reset(self):
		# Generate a random starting agent coordinate if we're supposed to
		if self._random_agent_pos:
			a_x = random.randint(0, const.MAP_WIDTH-1)
			a_y = random.randint(0, const.MAP_HEIGHT-1)
			self._agent = Object(True, x=a_x, y=a_y)
		# Default agent starting coordinates
		else: self._agent = Object(True)

		# Number of target objects to generate
		num_targets = const.NUM_TARGETS

		# Randomise the number of targets to generate if we're supposed to
		if self._random_num_targets:
			num_targets = rand.randint(const.NUM_TARGETS_RANGE[0], const.NUM_TARGETS_RANGE[1])

		# Initialise the targets list
		self._targets = []

		# Generate the targets
		for i in range(num_targets):
			t_x, t_y = self.generateUnoccupiedPosition()
			self._targets.append(Object(False, x=t_x, y=t_y))

		return self.getAgentPos()

	# Generate a random position within the grid that isn't already occupied
	def generateUnoccupiedPosition(self):
		# List of occupied positions
		occupied = []

		# Combine all generated positions up to this point
		occupied.append(self.getAgentPos())
		if self._targets is not None:
			for target in self._targets:
				occupied.append(target.getPosTuple())

		# Loop until we've generated a valid position
		while True:
			# Generate a position within bounds
			rand_x = random.randint(0, const.MAP_WIDTH-1)
			rand_y = random.randint(0, const.MAP_HEIGHT-1)

			ok = True

			# Check the generated position isn't already in use
			for pos in occupied:
				if rand_x == pos[0] and rand_y == pos[1]:
					ok = False
					break

			if ok: return rand_x, rand_y

	# Print coordinates of the agent and all targets
	def printObjectCoordinates(self):
		a_x, a_y = self._agent.getPos()
		print "Agent pos = ({},{})".format(a_x, a_y)

		for i in range(len(self._targets)):
			t_x, t_y = self._targets[i].getPos()
			print "Target #{} pos = ({},{})".format(i, t_x, t_y)

	# Update the position of the agent
	def updateAgentPos(self, x, y):
		self._agent.setPos(x, y)

	# Returns the coordinates of the closest target to the current agent position that
	# hasn't already been visited
	def findClosestTarget(self):
		# Get the current agent position
		a_x, a_y = self._agent.getPos()

		best_dist = float("inf")
		best_coords = (-1,-1)

		# Iterate over each target
		for target in self._targets:
			# Check that we haven't already visited this target
			if not target.visited:
				# Find the distance
				distance = Utility.distanceBetweenPoints((a_x, a_y), target)

				# Is the current distance better
				if distance < best_dist:
					best_dist = distance
					best_coords = target

		return best_coords

	# Returns True if all targets have been visited
	def allTargetsVisited(self):
		for target in self._targets:
			if not target.getVisited():
				return False

		return True

	# Simply returns the position of the agent
	def getAgentPos(self):
		return self._agent.getPos()

	# Set the position of agent, check whether it matches a target position
	def setAgentPos(self, x, y):
		# Set the position
		self._agent.setPos(x, y)

		self.checkAgentTargetMatch(x, y)

	# Marks a target as visited if the agent position matches it
	def checkAgentTargetMatch(self, a_x, a_y):
		for target in self._targets:
			t_x, t_y = target.getPos()

			if a_x == t_x and a_y == t_y:
				if not target.getVisited():
					target.setVisited(True)

	# Returns a list of all target positions
	def getTargetPositions(self):
		positions = []

		for target in self._targets:
			positions.append(target.getPosTuple())

		return positions

# Entry method for unit testing
if __name__ == '__main__':
	object_handler = ObjectHandler()
	object_handler.printObjectCoordinates()