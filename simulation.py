import math
import json
import random

class MonteCarlo:
    
	def __init__(self, number_of_iterations):
		self.radius = 10
		self.a = 10
		self.center_of_circle = (50, 25)
		self.x_max_board = 80
		self.y_max_board = 50
		self.x_min_square = 10
		self.x_max_square = 20
		self.y_min_square = 10
		self.y_max_square = 20
		self.balls_inside_circle = 0
		self.balls_inside_square = 0
		self.simulation_data = []
		self.iterations = number_of_iterations
	
	def get_random_coordinates(self):
		random_x = random.random()
		random_y = random.random()
		return (round(random_x*self.x_max_board, 2), round(random_y*self.y_max_board, 2))
	
	def is_inside_circle(self, random_coordinates):
		(x, y) = random_coordinates
		(xc, yc) = self.center_of_circle

		distance_from_center_of_circle = math.sqrt((xc-x)**2 + (yc-y)**2)

		if distance_from_center_of_circle>self.radius:
			return False
		return True
	
	def is_inside_square(self, random_coordinates):
		(x, y) = random_coordinates

		if (x>=self.x_min_square and x<=self.x_max_square and y>=self.y_min_square and y<=self.y_max_square):
			return True
		return False
	
	def simulate(self, i):
		random_coordinates = self.get_random_coordinates()

		inside_circle = self.is_inside_circle(random_coordinates)
		inside_square = self.is_inside_square(random_coordinates)

		if (inside_circle):
			self.balls_inside_circle += 1
		
		elif (inside_square):
			self.balls_inside_square += 1
		
		self.simulation_data.append({
			"iteration": i,
			"num_balls_square": self.balls_inside_square,
			"num_balls_circle": self.balls_inside_circle
		})

		ratio = 0

		if (self.balls_inside_square!=0):
			ratio = self.balls_inside_circle/self.balls_inside_square

		print(f"Current Ratio : {ratio}")
		
	
	def __call__(self):

		print("---------SIMULATION STARTS--------------")

		for i in range(self.iterations):
			self.simulate(i)
		
		print("---------SIMULATION COMPLETE--------------")

		with open("./data.json", "w") as f:
			json.dump(self.simulation_data, f)

obj = MonteCarlo(1000000)
obj()