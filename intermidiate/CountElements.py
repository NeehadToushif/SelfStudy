class Solution:
    # @param A : integer
    # @return an integer
    def solve(self,A):
        cnt = 0
        max = A[0]
        for i in A:
            if i > max:
                max = i
        for j in A:
            if max == j:
                cnt+=1
        return len(A)-cnt
sol = Solution()
print(sol.solve([0,1,3,4,4,4]))

