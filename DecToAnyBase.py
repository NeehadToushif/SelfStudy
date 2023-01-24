class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum = 0
        for i,e in enumerate(reversed(str(A))):
            sum = sum + int(e)*B**i
        return sum

    def solve2(self,A,B):
        i = 0
        sum = 0

        while(A>0):
            num = A%B
            A = int(A/B)
            sum = sum + num*10**i
            i+=1
        return sum


# print(Solution().solve(1010,2))
print(Solution().solve2(76,2))