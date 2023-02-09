class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        binArr = []
        for i in A:
            if i%2==0:
                binArr.append(1)
            else:
                binArr.append(0)
        pfSum = [binArr[0]]
        for i in range(1, len(binArr)):
            pfSum.append(pfSum[i - 1] + binArr[i])
        # print(A)
        # print(binArr)
        # print(pfSum)
        result =[]
        for q in B:
            L= q[0]
            R= q[1]
            if L == 0:
                sum = pfSum[R]
            else:
                sum = pfSum[R] - pfSum[L-1]
            result.append(sum)
        return result

print(Solution().rangeSum([1, 2, 3, 4, 5],[
    [0, 2],
    [1, 4]
]))