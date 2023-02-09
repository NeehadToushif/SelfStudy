class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def checkBit(self,A,i):
        return A>>i & 1
    def solve(self, A, B):
        if self.checkBit(A,B):
            return A ^ 1<<B
        else:
            return A

print(Solution().solve(10, 3))