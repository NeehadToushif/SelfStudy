class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sum = 0
        for i in range(1,A):
            if i < A / i:
                if A%i == 0:
                    sum = sum+i+A/i
            else:
                break
        if (sum - A) == A:
            return 1
        else:
            return 0

sol = Solution()
print(sol.solve(8120))