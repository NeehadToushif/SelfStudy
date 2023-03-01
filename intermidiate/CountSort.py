'''Problem Description
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        count = [0 for i in range(max(A)+1)]
        ans = []
        for i in A:
            count[i]+=1
        for idx,val in enumerate(count):
            if val>0:
                for c in range(val):
                    ans.append(idx)
        return ans
A = [1, 3, 1]
A = [10, 2, 1, 3]
print(Solution().solve(A))