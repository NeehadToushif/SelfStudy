class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A):
        for i in range(1, len(A)):
            A[i] = (A[i - 1] + A[i])
        return A

print(Solution().rangeSum([1, 2, 3, 4, 5]))