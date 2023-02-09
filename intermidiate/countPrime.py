class Solution:
    # @param A : integer
    # @return an integer
    def checkPrime(self,N):
        cnt = 0
        if N <= 1:
            return 0
        i = 1
        while i <= N / i:
            if N % i == 0:
                if i < N / i:
                    cnt = cnt + 2
                else:
                    cnt = cnt + 1
            i += 1
        if cnt > 2:
            return 0
        else:
            return 1
    def solve(self, A):
        count = 0
        if A<=1:
            return count
        else:
            for i in range(1,A+1):
                if self.checkPrime(i):
                    count+=1
            return count
sol = Solution()
print(sol.solve(1000))