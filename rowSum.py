class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        i = 0
        sum_arr = []
        while i < row:
            j = 0
            sum = 0
            while j<col:
                sum = sum + A[i][j]
                j+=1
            sum_arr.append(sum)
            i+=1
        return sum_arr



A = [[1,2,3,4],
     [5,6,7,8],
     [9,2,3,4]]
print(Solution().solve(A))