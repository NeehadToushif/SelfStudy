''' Problem Description
Given an array of integers, every element appears thrice except for one, which occurs once.

Find that element that does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?




Problem Constraints
2 <= A <= 5*106

0 <= A <= INTMAX'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
    def checkBit(self,num,i):
        return num>>i &1
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            sum = 0
            for j in A:
                if self.checkBit(j,i):
                    sum+=1
            if sum%3 ==1:
                ans = ans+(1<<i)
        return ans




A =[0, 0, 0, 1]
A =[1, 2, 5, 3, 3, 2, 2, 3, 1, 1]
print(Solution().singleNumber(A))