''' Problem Description
Given an array A. For every pair of indices i and j (i != j), find the maximum A[i] & A[j].


Problem Constraints
1 <= len(A) <= 105
1 <= A[i] <= 109'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def checkBit(self,num,i):
        return num>>i & 1
    def solve(self, A):
        ans = 0
        for i in range(30,-1,-1):
            # print(i)
            c = 0
            for j in A:
                if self.checkBit(j,i):
                    c+=1
            if c>=2:
                ans = ans + (1<<i)
                for j in range(len(A)):
                    if not self.checkBit(A[j],i):
                        A[j]=0
        return ans

A = [53, 39, 88]
print(Solution().solve(A))