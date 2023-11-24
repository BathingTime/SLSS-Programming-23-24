# Functions
# Sunny Lin
# Nov 24, 23

def print_area_of_a_square(sidelength:float):
	'''
	Calculate and print the area of a square.
	Results are in units squared.
	
	Params:
	• sidelength = length of one side of the square.
	'''
	
	area=sidelength**2
	
	print(f'The area of a square with side length {sidelength} is {area} square units.')

def area_of_a_square(sidelength:float)->float:
	'''
	Calculate and returns the area of a square.
	Results are in units squared.
	
	Params:
	• sidelength = length of one side of the square.
	'''
	
	area=sidelength**2
	
	return area

print(print_area_of_a_square(12.2))
print(print_area_of_a_square(12))

print(area_of_a_square(12.2))
print(area_of_a_square(12))

# Given two squares of two sidelengths (12.2 and 144), add the area of both squares.
area_of_squares=area_of_a_square(12.2)+area_of_a_square(144)
print(area_of_squares)