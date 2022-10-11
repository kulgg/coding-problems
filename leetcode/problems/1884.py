from cmath import sqrt
from math import ceil, floor


class Solution:
	"""
	Leetcode Problem #1884

	Topics: Dynamic Programming
	"""
	def twoEggDrop(self, n: int) -> int:
		# linear drops
		# x^2 + x - 2*n = 0
		# x = - 1 / 2 + sqrt(1/4 + 2*n)
		return ceil(- 1 / 2 + sqrt(1/4 + 2*n).real)

if __name__ == "__main__":
	sol = Solution()
	assert sol.twoEggDrop(1) == 1
	assert sol.twoEggDrop(2) == 2
	assert sol.twoEggDrop(100) == 14

	
