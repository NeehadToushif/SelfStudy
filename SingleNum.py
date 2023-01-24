class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        n = 0
        for i in A:
            n = n^i
        return n
print(Solution().singleNumber([1,2,2,3,1,3,4]))