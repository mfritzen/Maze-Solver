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

if __name__ == "__main__":
	maze = getMaze("maze.txt")
	end_point = getCoord(maze, "E")
	start_point = getCoord(maze, "S")