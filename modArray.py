class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        exp = 1
        n = len(A)
        # for i,d in enumerate(A):
        #     ans = (ans + (d*10**(n-i-1))%B )%B
        # return ans
        for i in range(n-1,-1,-1):
            temp = A[i]*exp % B
            ans = (ans+temp) % B
            exp = exp*10 % B
        return ans
A = [4, 3, 5, 3, 5, 3, 2, 1]
B = 47
print(Solution().solve(A,B))