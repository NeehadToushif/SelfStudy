class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        if len(A) % 2 != 0 or A[0] % 2 != 0 or A[len(A) - 1] % 2 != 0:
            return 'NO'
        return 'YES'

print(Solution().solve([2, 1, 3, 1, 5, 1, 1,8]))