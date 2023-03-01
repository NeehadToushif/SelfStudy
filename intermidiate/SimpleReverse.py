'''Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        return (''.join(reversed(A)))
A = "scaler"
print(Solution().solve(A))
print("Aa".swapcase())