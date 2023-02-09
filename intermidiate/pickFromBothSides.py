class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        pf = [0,A[0]]
        revA = list(reversed(A))
        sf = [0,revA[0]]
        for i in range(1,len(A)):
            pf.append(pf[i]+A[i])
        for i in range(1, len(A)):
            sf.append(sf[i] + revA[i])
        i=B
        j=0
        _max = pf[B]
        while i>=0:
            newSum = pf[i]+sf[j]
            i-=1
            j+=1
            if newSum>_max:
                _max = newSum
        return _max
print(Solution().solve([3,0,0,0,1,1],3))