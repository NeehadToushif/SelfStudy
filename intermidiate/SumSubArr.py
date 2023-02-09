class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        sum = 0
        n = len(A)
        for i in range(n):
            totCon = (i+1)*(n-i)
            sum = sum + totCon*A[i]
        print(sum)

print(Solution().subarraySum([1,2,3]))