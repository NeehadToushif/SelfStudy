''' Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



Problem Constraints
1 <= |A| <= 2000000

0 <= A[i] <= INTMAX'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1,len(A)):
            ans = ans ^ A[i]
        return ans


A = [1, 2, 2, 3, 1]
A = [1, 2, 2]


print(Solution().singleNumber(A))