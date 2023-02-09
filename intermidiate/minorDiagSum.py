class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        m = len(A)
        sum = 0
        for i in range(1,m+1):
            j = m+1-i
            sum = sum + A[i-1][j-1]
        return sum


A = [[3, 3],
     [2, 3]]
print(Solution().solve(A))

