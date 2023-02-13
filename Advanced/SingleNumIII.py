''' Problem Description
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.


Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def checkBit(self,num,i):
        return num>>i & 1
    def solve(self, A):
        XOR = 0
        setBit = -1
        for i in A:
            XOR^=i
        for i in range(30):
            if self.checkBit(XOR,i):
                setBit = i

        buc1,buc2=0,0
        for i in A:
            if self.checkBit(i,setBit):
                buc1^=i
            else:
                buc2^=i

        return [min(buc1,buc2),max(buc1,buc2)]



A = [1, 2, 3, 1, 2, 4]
A = [1, 2]
print(Solution().solve(A))