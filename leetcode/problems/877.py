from cmath import sqrt
from math import ceil, floor
from typing import List


class Solution:
	"""
	Leetcode Problem #877

	Topics: Dynamic Programming
	"""
	def stoneGame(self, piles: List[int]) -> bool:
		return True

 
def test_a():
	sol = Solution()
	assert sol.stoneGame([5,3,4,5])
	assert sol.stoneGame([3,7,2,3])
	