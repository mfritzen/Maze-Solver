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

	maze = removeJunk(maze, "U")
	writeSol("maze_solution.txt", maze)