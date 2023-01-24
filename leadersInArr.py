class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        max = A[n-1]
        ans =[max]

        for i in range(n-1,0,-1):
            if A[i]>max:
                max = A[i]
                ans.append(max)
        return ans

print(Solution().solve([16, 17, 4, 3, 5, 2]))