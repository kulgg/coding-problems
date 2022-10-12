from cmath import sqrt
from math import ceil, floor
from typing import List


class Solution:
	"""
	Leetcode Problem #877

	Topics: Dynamic Programming
	"""
	def stoneGame(self, piles: List[int], alice_sum: int = 0, bob_sum: int= 0, aliceTurn: bool = True) -> bool:
		n = len(piles)		
		if n == 1:
			return alice_sum > bob_sum + piles[0]
		
		if aliceTurn:
			result = (self.stoneGame(piles[1:], alice_sum + piles[0], bob_sum, not aliceTurn)
				or self.stoneGame(piles[:-1], piles[n-1] + alice_sum, bob_sum, not aliceTurn) )
			self.cache[piles] = result
		else:
			return (self.stoneGame(piles[1:], alice_sum, piles[0] + bob_sum, not aliceTurn)
			or self.stoneGame(piles[:-1], alice_sum, bob_sum + piles[n-1] , not aliceTurn) )

 
def test_a():
	sol = Solution()
	assert sol.stoneGame([5,3,4,5])
	assert sol.stoneGame([3,7,2,3])
	