class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        Ta =  [ [0]*r for i in range(c)]

        for i in range(r):
            for j in range(0,c):
                Ta[j][i]=A[i][j]
        return Ta

A = [
    [1,2,3],
    [4,5,6]

]
print(Solution().solve(A))