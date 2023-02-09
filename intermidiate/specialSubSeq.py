class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        cnt = 0
        #pf sum of A
        if A[0]=='A':
            pfA = [1]
        else:
            pfA = [0]
        for i in range(1,len(A)):
            if A[i]=='A':
                pfA.append(pfA[i-1]+1)
            else:
                pfA.append(pfA[i-1])
        print(pfA)
        for i in range(len(A)):
            if A[i]=='G':
                cnt = cnt+pfA[i]

        return cnt

print(Solution().solve("ABCGAG"))