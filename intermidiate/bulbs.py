class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
            prev = 1
            cnt = 0
            for i in range(len(A)):
                if A[i] != prev:
                    cnt += 1
                    prev = A[i]
            return cnt

print(Solution().bulbs([0,0,0,0,0]))