'''
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        carry = 0
        ans = float("-inf")
        for i in range(len(A)):
            sum = carry+A[i]
            ans = max(ans,sum)
            carry = sum
            carry = 0 if sum<0 else carry

        return ans

A = [-500]
print(Solution().maxSubArray(A))