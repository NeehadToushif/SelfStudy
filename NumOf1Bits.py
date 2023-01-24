class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        cnt = 0
        while A>0:
            if A&1:
                cnt+=1
            A = A>>1
        return cnt
print(Solution().numSetBits(6))