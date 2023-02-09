class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        pfSum = [A[0]]
        for i in range(1, len(A)):
            pfSum.append(pfSum[i - 1] + A[i])
        result =[]
        for q in B:
            L= q[0]-1
            R= q[1]-1
            if L == 0:
                sum = pfSum[R]
            else:
                sum = pfSum[R]- pfSum[L-1]
            result.append(sum)
        return result

print(Solution().rangeSum([7, 3, 1, 5, 5, 5, 1, 2, 4, 5],[
  [7, 10],
  [3, 10],
  [3, 5],
  [1, 10]
]))