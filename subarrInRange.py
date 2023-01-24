class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        return A[B:C+1]
    
print(Solution().solve([1,2,3,4,5,6,7],2,3))