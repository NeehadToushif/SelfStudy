''' Problem Description
Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints
1 <= A <= 109'''
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A>0:
            if A & 1:
                count = count + 1
            A =A>>1
        return count


A =7
print(Solution().numSetBits(A))