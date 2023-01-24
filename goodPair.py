class Solution:
    # @param A : integer
    # @return an integer

    def solve(self,A,B):
        i = 0
        while i<len(A):
            j = i+1
            while j<len(A):
                if A[i]+A[j] == B:
                    return 1
                else:
                    j+=1
            i+=1
        return 0
sol = Solution()
print(sol.solve([0,1,3,2,3,4],6))

