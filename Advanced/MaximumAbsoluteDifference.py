'''Problem Description
You are given an array of N integers, A1, A2, .... AN.

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.



Problem Constraints
1 <= N <= 100000

-109 <= A[i] <= 109'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        X = []
        Y = []
        for i,val in enumerate(A):
            X.append(i+val)
            Y.append(val-i)
      
        return max(max(X)-min(X),max(Y)-min(Y))

A = [1, 3, -1]
print(Solution().maxArr(A))