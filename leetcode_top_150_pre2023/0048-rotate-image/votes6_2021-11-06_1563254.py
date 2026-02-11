def rotate(self, matrix: List[List[int]]) -> None:
	matrix[:] = np.rot90(matrix, axes=(1, 0))