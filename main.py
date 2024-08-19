import random, math, render_maze, time, os, keyboard

class Cell:
	def __init__(self):
		self.walls = {'top':True, 'right':True, 'bottom':True, 'left':True}
		self.visited = False



def gen_field(w, h):
	field = []
	for y in range(h):
		field.append([])
		for x in range(w):
			field[y].append(Cell())

	return field

def get_neighbors(pos, field): #returns POSITIONS of neighbors
	neighbors = []
	if pos[0] > 0:
		if not field[pos[1]][pos[0]-1].visited:
			neighbors.append([pos[0]-1, pos[1]])

	if pos[0] < len(field[0])-1:
		if not field[pos[1]][pos[0]+1].visited:
			neighbors.append([pos[0]+1, pos[1]])

	if pos[1] > 0:
		if not field[pos[1]-1][pos[0]].visited:
			neighbors.append([pos[0], pos[1]-1])

	if pos[1] < len(field)-1:
		if not field[pos[1]+1][pos[0]].visited:
			neighbors.append([pos[0], pos[1]+1])

	return neighbors

def generate(w, h, starting_pos=[0,0], steps=False):
	os.system('cls')
	field = gen_field(w,h)
	stack = [starting_pos]

	step_delay = 0
	delay = step_delay*1

	current = stack[0]
	visited = 1
	field[current[1]][current[0]].visited = True

	farthest_point_tup = ([0,0], 0)
	for i in range(100000):
		neighbors = get_neighbors(current, field)

		if len(neighbors) == 0:
			# propogates backwards, stops if it gets to beginning
			current = stack.pop()
			#print('DEAD END')
			if current == starting_pos:
				break

		else:
			chosen = random.choice(neighbors)

			# changing walls
			if chosen[0] > current[0]:
				field[chosen[1]][chosen[0]].walls['left'] = False
				field[current[1]][current[0]].walls['right'] = False
				#print('WENT RIGHT')
			elif chosen[0] < current[0]:
				field[chosen[1]][chosen[0]].walls['right'] = False
				field[current[1]][current[0]].walls['left'] = False
				#print('WENT LEFT')
			elif chosen[1] > current[1]:
				field[chosen[1]][chosen[0]].walls['top'] = False
				field[current[1]][current[0]].walls['bottom'] = False
				#print('WENT DOWN')
			else:
				field[chosen[1]][chosen[0]].walls['bottom'] = False
				field[current[1]][current[0]].walls['top'] = False
				#print('WENT UP')

			field[chosen[1]][chosen[0]].visited = True
			visited += 1
			stack.append(current)
			if len(stack) > farthest_point_tup[1]:
				farthest_point_tup = (chosen, len(stack))

			
			#print(f'Current: {current}')
			#print(f'Chosen: {chosen}')
			current = chosen
			chosen = None

		if visited >= w*h:
			break

		
		if steps:
			if delay <= 0:
				os.system('cls')
				maze = render_maze.create_field(field, '██', '  ', current)
				render_maze.render(maze)#█
				#while not keyboard.is_pressed('ESC'):
					#pass
				#while keyboard.is_pressed('ESC'):
					#pass
				time.sleep(0.5)
				delay = step_delay*1
			else:
				delay -= 1


	return field, farthest_point_tup



#maze = generate(51,30)
maze, farthest = generate(51, 25, steps=True)
end_point = farthest[0]
maze = render_maze.create_field(maze, '██', '  ', end_point)
os.system('cls')
render_maze.render(maze)#█


