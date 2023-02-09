'''
Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

Problem Constraints
1 <= N <=30

0 <= A[i][j] <= 10
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        sum = 0
        for i in range(n):
            for j in range(n):
                contrib = (i+1)*(j+1)*(n-i)*(n-j)
                sum = sum + A[i][j]*contrib
        return sum
A =   [ [1, 2],
      [3, 4] ]
print(Solution().solve(A=A))