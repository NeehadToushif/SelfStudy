class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A==B:
            return 1<<A
        else:
            return (1<<A)+(1<<B)

print(Solution().solve(4,4))

