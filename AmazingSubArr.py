class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        vowel = "AEIOUaeiou"
        n = len(A)
        for i in range(n):
            if A[i] in vowel:
                print(A[i])
                count = count + n-i
        return count % 10003
print(Solution().solve("Aabei"))