from typing import List

a = [[1, 1, 0],
     [1, 0, 2]]

b = [[1, 0, 2, 1],
     [2, 1, 2, 0],
     [1, 1, 0, 3]]
def vec_product(vec1: List[int], vec2: List[int]) -> int:
    return sum([int(x * y) for x, y in zip(vec1, vec2)])


def matrix_transpose(mat: List[List]) -> List[List]:
    return [*map(list, zip(*mat))]


def matrix_product(mat1: List[List[int]], mat2: List[List[int]]):
    l, n = len(mat1), len(mat2[0])
    ans = [[0 for i in range(n)] for j in range(l)]
    for i in range(l):
        for j in range(n):
            vec1 = mat1[i]
            vec2 = matrix_transpose(mat2)[j]
            ans[i][j] = vec_product(vec1, vec2)
    return ans

print(matrix_product(a,b))