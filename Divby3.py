class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sum = 0
        for i in A:
            sum = sum+i
        if sum%3 == 0:
            return 1
        else:
            return 0


A = [1,2,3]
print(Solution().solve(A))