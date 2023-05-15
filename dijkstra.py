import math


def check_vertex(line, vertex):
    for i in range (len(line)):
        if line[i] + tags[vertex-1] < tags[i] and line[i] != 0 and (i+1) not in visited:
            tags[i] = line[i] + tags[vertex-1]

def check_min():
    min_ind = -1
    max_value = math.inf
    for k in range(len(tags)):
        if tags[k] < max_value and (k + 1) not in visited:
            max_value = tags[k]
            min_ind = k + 1
    return min_ind


matrix = [
    #1  2  3  4  5  6
    [0, 7, 9, 0, 0, 14], #1
    [7, 0, 10, 15, 0, 0], #2
    [9, 10, 0, 11, 0, 2], #3
    [0, 15, 11, 0, 6, 0], #4
    [0, 0, 0, 6, 0, 9], #5
    [14, 0, 2, 0, 9, 0]  #6
]

visited = set()
tags = [0]
for i in range(len(matrix)-1):
    tags.append(math.inf)
check_vertex(matrix[0], 1)
visited.add(1)
for l in range(len(matrix)-1):
    min_index = check_min()
    visited.add(min_index)
    check_vertex(matrix[min_index-1], min_index)

print(tags)
