'''
Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.

Problem Constraints
1 <= N <= 1000000

-109 <= A[i] <= 10^9
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def swap(self,A,i,j):
        A[i],A[j] = A[j],A[i]
        return A
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n-1):
            while (A[i]!=i+1 and A[i]>0 and A[i]<=n):
                x = A[i]
                if x==A[x-1]:
                    break
                A = self.swap(A,i,x-1)
        for i in range(n):
            if A[i] != i+1:
                return i+1
        return n+1
A = [-8, -7, -6]
print(Solution().firstMissingPositive(A))