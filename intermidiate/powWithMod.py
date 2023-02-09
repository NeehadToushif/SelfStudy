class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ans = 1
        for i in range(B):
            ans = (ans*A%C)%C
        return ans

print(Solution().solve(2,3,3))