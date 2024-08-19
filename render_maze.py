import os, sys

def gen_field(w, h, v):
	field = []
	for y in range(h):
		field.append([])
		for x in range(w):
			field[y].append(v)

	return field

def old_render(field, fill, empty):
	for y in range(len(field)*2):
		for x in range(len(field[int(round(y/2))])*2):
			lx, ly = int(round(x/2)), int(round(y/2))
			print(f'x: {x}, y: {y}')
			print(f'X: {lx}, Y: {ly}')

			if y % 2 == 0:
				sys.stdout.write(fill)
				sys.stdout.write(fill if not field[ly][lx].walls['top'] else empty)
			else:
				if field[ly][lx].walls['left']:
					sys.stdout.write(fill)
				else:
					sys.stdout.write(empty)
				sys.stdout.write(empty)

		if y % 2 == 0:
			sys.stdout.write(fill)
		else:
			if field[ly][lx].walls['right']:
				sys.stdout.write(fill)
			else:
				sys.stdout.write(empty)

		sys.stdout.write('\n')
		sys.stdout.flush()


	for x in range(len(field[0])*2):
		if x % 2 == 0:
			sys.stdout.write(fill)
		else:
			sys.stdout.write(fill if not field[-1][round(x/2)].walls['bottom'] else empty)

	sys.stdout.write(fill)

def create_field(field, fill, empty, chosen=None):
	screen_field = gen_field(len(field[0])*2+1, len(field)*2+1, fill)
	for y in range(len(field)):
		for x in range(len(field[y])):
			cell = field[y][x]
			screen_pos = [x*2+1, y*2+1]

			for sy in range(-1,2):
				for sx in range(-1,2):
					cell_spos =	[screen_pos[0] + sx, screen_pos[1] + sy]
					#print(f'SX: {sx}, SY: {sy}')
					if [sx,sy] == [-1,-1] or [sx,sy] == [1,-1] or [sx,sy] == [-1,1] or [sx,sy] == [1,1]:
						screen_field[cell_spos[1]][cell_spos[0]] = fill
						#print('filled')

					else:
						if sx == -1:
							if cell.walls['left']:
								screen_field[cell_spos[1]][cell_spos[0]] = fill
							else:
								screen_field[cell_spos[1]][cell_spos[0]] = empty
						elif sx == 1:
							if cell.walls['right']:
								screen_field[cell_spos[1]][cell_spos[0]] = fill
							else:
								screen_field[cell_spos[1]][cell_spos[0]] = empty
						elif sy == -1:
							if cell.walls['top']:
								screen_field[cell_spos[1]][cell_spos[0]] = fill
							else:
								screen_field[cell_spos[1]][cell_spos[0]] = empty
						elif sy == 1:
							if cell.walls['bottom']:
								screen_field[cell_spos[1]][cell_spos[0]] = fill
							else:
								screen_field[cell_spos[1]][cell_spos[0]] = empty

						else:
							if [x,y] == chosen:
								screen_field[cell_spos[1]][cell_spos[0]] = ':)'

							else:
								screen_field[cell_spos[1]][cell_spos[0]] = empty
						#print('empty')

	return screen_field


	#print(screen_field)		


def render(maze):
	screen_field = maze
	for y in range((len(screen_field))):
		for x in range(len(screen_field[y])):
			sys.stdout.write(screen_field[y][x])

		sys.stdout.write('\n')
		sys.stdout.flush()








