'''
Problem Description
Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom, and columns are numbered from left to right.
Sum may be large, so return the answer mod 109 + 7.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M
'''
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        #find prefixsum arr
        n = len(A)
        m = len(A[0])
        pf = [[0 for col in range(m)] for row in range(n)]
        pf[0][0] = A[0][0]
        for i in range(n):
            for j in range(1,m):
                pf[i][j]=(A[i][j] + pf[i][j-1])
        print(pf)
        pf2= [[pf[row][col] for col in range(m)] for row in range(n)]
        for i in range(1,n):
            for j in range(m):
                pf2[i][j] = pf[i][j] + pf2[i-1][j]
        ans = []

        print(pf2)
        for q in zip(B,C,D,E):
            b,c,d,e = q
            b=b-1
            c=c-1
            d=d-1
            e=e-1
            X = pf[b-1][e] if b>0 else 0
            Y = pf[d][c-1] if c>0 else 0
            Z = pf[b-1][c-1] if b>0 and c>0 else 0
            ans = pf[d][e] - X - Y + Z
            # ans.append(pf[d][e] - X - Y + Z)
            print("{}-{}-{}+{} =  ".format(pf[d][e] , X ,Y,Z,ans))
        return ans
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]
print(Solution().solve(A, B, C, D, E))