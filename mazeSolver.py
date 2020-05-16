done = False

def getMaze(filename):
	
	maze = []

	with open(filename) as fp:
		while (1):
			next_line = fp.readline()
			next_line.rstrip()
			if not next_line:
				break
			maze.append(next_line)

	return maze

def getCoord(maze, target):

	still_going = True

	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == target:
				still_going = False
				break
		if still_going == False:
			break

	return (i, j)

def makeMazeList(maze):
	maze_as_list = []
	for line in maze:
		line_as_list = []
		for block in line:
			line_as_list.append(block)
		maze_as_list.append(line_as_list)
	return maze_as_list

def solveMaze(maze, start, end):
	x = start[1]
	y = start[0]

	# go north
	maze = solveRecurse(maze, (y-1, x), 0)
	# go east
	maze = solveRecurse(maze, (y, x+1), 1)
	# go south
	maze = solveRecurse(maze, (y+1, x), 2)
	# go west
	maze = solveRecurse(maze, (y, x-1), 3)

	return maze

def solveRecurse(maze, coord, direction):
	y = coord[0]
	x = coord[1]
	path_char = "o"

	if ((y < 0) or (y >= len(maze)) or (x < 0) or (x >= len(maze[0]))):
		return maze
	if maze[y][x] == "X":
		return maze
	if maze[y][x] == "U":
		return maze
	
	if maze[y][x] == "E":
		maze[y][x] = path_char
		global done
		done = True
		return maze

	if maze[y][x] == " ":
		maze[y][x] = "U"
		if direction == 0: # previous move was north
			maze = solveRecurse(maze, (y-1, x), 0) # go north
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y, x+1), 1) # go east
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y, x-1), 3) # go west
			if done == True:
				maze[y][x] = path_char
				return maze
		if direction == 1: # previous move was east
			maze = solveRecurse(maze, (y-1, x), 0) # go north
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y, x+1), 1) # go east
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y+1, x), 2) # go south
			if done == True:
				maze[y][x] = path_char
				return maze
		if direction == 2: # previous move was south
			maze = solveRecurse(maze, (y, x+1), 1) # go east
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y+1, x), 2) # go south
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y, x-1), 3) # go west
			if done == True:
				maze[y][x] = path_char
				return maze
		if direction == 3: # previous move was west
			maze = solveRecurse(maze, (y-1, x), 0) # go north
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y+1, x), 2) # go south
			if done == True:
				maze[y][x] = path_char
				return maze
			maze = solveRecurse(maze, (y, x-1), 3) # go west
			if done == True:
				maze[y][x] = path_char
				return maze
		
	if done == True:
		maze[y][x] = path_char
	return maze

def removeJunk(maze, junk):
	clean_maze = []
	for line in maze:
		clean_line = []
		for block in line:
			if block == junk:
				clean_line.append(" ")
			else:
				clean_line.append(block)
		clean_maze.append(clean_line)
	return clean_maze

def writeSol(filename, solution):
	with open(filename, "w") as fp:
		for line in solution:
			for block in line:
				fp.write(str(block))
	return

if __name__ == "__main__":
	maze = getMaze("maze.txt")
	end_point = getCoord(maze, "E")
	start_point = getCoord(maze, "S")
	maze = makeMazeList(maze)
	maze = solveMaze(maze, start_point, end_point)
	maze = removeJunk(maze, "U")
	writeSol("maze_solution.txt", maze)