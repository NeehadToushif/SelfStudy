''' Problem Description
sum of all xor for all pairs

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
        for i in range(30):
            cnt = 0
            for j in A:
                if self.checkBit(j,i):
                    cnt+=1
            contri = cnt * (len(A)-cnt)
            ans = ans + contri *(1<<i)
        return ans*2

A = [53, 39, 88]
print(Solution().solve(A))