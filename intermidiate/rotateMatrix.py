class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i,n):
                A[i][j],A[j][i]=A[j][i],A[i][j]
        # print(A)
        for i in range(n):
            s = 0
            e = n-1
            while (s<e):
                A[i][s],A[i][e] = A[i][e],A[i][s]
                # print(i,s,'&',e,i)
                s+=1
                e-=1
        return A
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(Solution().solve(A))