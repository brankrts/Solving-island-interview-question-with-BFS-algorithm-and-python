
array = [

    [1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1]

]


def findPath():
    queue = []
    possiblePaths = []
    corners = fine_corners()
    actualPath = []
    white = -1
    black = 1

    for i in range(len(array)):
        for j in range(len(array[0])):
            possiblePaths.append([i, j, white, array[i][j]])
    for x, y in corners:
        for i in possiblePaths:
            if i[0] == x and i[1] == y:
                queue.append(i)
                actualPath.append(i)
    while len(queue) != 0:
        x, y, color, _ = queue.pop(0)
        index = x*6 + y
        if color != black:
            find_real_path(index, color, possiblePaths, actualPath, queue)
        possiblePaths[index][2] = black
    print(actualPath)


def find_real_path(index, color, possiblePaths, actualPath, queue):
    gray = 0
    black = 1
    if color != black:
        if (index % len(array) < len(array[0])-1 and possiblePaths[index+1][len(possiblePaths[0])-1] == 1):
            queue.append(possiblePaths[index+1])
            possiblePaths[index+1][2] = gray

            if not contain(actualPath, possiblePaths[index+1]):
                actualPath.append(possiblePaths[index+1])
                find_real_path(index, color, possiblePaths,
                               actualPath, queue)
        if(index % len(array) > 0 and possiblePaths[index-1][len(possiblePaths[0])-1] == 1 and not contain(actualPath, possiblePaths[index-1])):
            queue.append(possiblePaths[index-1])
            possiblePaths[index-1][2] = gray

            if not contain(actualPath, possiblePaths[index-1]):
                actualPath.append(possiblePaths[index-1])
                find_real_path(index, color, possiblePaths,
                               
                               actualPath, queue)
        if (index < len(possiblePaths)-1-len(array[0]) and possiblePaths[index+len(array)][len(possiblePaths[0])-1] == 1 and not contain(actualPath, possiblePaths[index+len(array)])):
            queue.append(possiblePaths[index+len(array)])
            possiblePaths[index+len(array)][2] = gray

            if not contain(actualPath, possiblePaths[index+len(array)]):
                actualPath.append(possiblePaths[index+len(array)])
                find_real_path(index, color, possiblePaths,
                               actualPath, queue)
                
        if(index > 0 and possiblePaths[index-len(array)][len(possiblePaths[0])-1] == 1 and not contain(actualPath, possiblePaths[index-len(array)])):
            queue.append(possiblePaths[index-len(array)])
            possiblePaths[index-len(array)][2] = gray

            if not contain(actualPath, possiblePaths[index-len(array)]):
                actualPath.append(possiblePaths[index-len(array)])
                find_real_path(index, color, possiblePaths,
                               actualPath, queue)


def contain(array, element):
    for x in array:
        if x == element:
            return True
    return False


def fine_corners():
    corners = []
    for i in range(len(array)):

        for j in range(len(array[0])):

            if ((j == len(array[0])-1 or j == 0 or i == 0 or i == len(array)-1) and array[i][j] == 1):
                corners.append([i, j])
    return corners


findPath()
