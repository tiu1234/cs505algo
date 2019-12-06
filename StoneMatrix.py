'''
Given an N X N matrix of stones like the following:

1s represent the stones, 0s represent empty spaces
As long as there are other stones on the same row or column, you can pick up that stone and throw it away.
Otherwise, you have to keep it.
What's the minium number of stones you can keep within the matrix.

For example:
1 1 0
1 0 0
0 0 0
 ||
 \/
1 0 0
1 0 0
0 0 0
 ||
 \/
1 0 0
0 0 0
0 0 0
 ||
 \/
1

Input:
1 0 0 1
1 0 0 0
1 0 0 0
0 1 0 0
Output:
2

Input:
1 1 0 1
1 0 0 0
1 0 0 0
0 0 0 0
Output:
1
'''

def stoneMatrix(matrix):
    count = 0

    m = len(matrix)
    n = len(matrix[0])
    visited = [[0] * n for i in range(m)]

    def bfs(a, b):
        visited[a][b] = 1
        queue = []

        for i in range(m):
            if matrix[i][b] == 1 and visited[i][b] == 0:
                visited[i][b] = 1
                queue.append((i, b))

        for j in range(n):
            if matrix[a][j] == 1 and visited[a][j] == 0:
                visited[a][j] = 1
                queue.append((a, j))

        for i, j in queue:
            bfs(i, j)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    return count


matrix = [[1,0,0,1],[1,0,0,0],[1,0,0,0],[0,1,0,0]]
print(stoneMatrix(matrix))
matrix = [[1,1,0,1],[1,0,0,0],[1,0,0,0],[0,1,0,0]]
print(stoneMatrix(matrix))
matrix = [[1,1,0,1],[1,0,0,0],[1,0,0,0],[0,0,1,0]]
print(stoneMatrix(matrix))