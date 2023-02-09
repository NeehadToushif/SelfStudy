class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        n = A
        pfsum = [C[0]]
        max_sum = 0
        all_sum = []
        for i in range(1,n):
            pfsum.append(pfsum[i-1]+C[i])
        for i in range(n):
            for j in range(i,n):
                if i == 0:
                    sum = pfsum[j]
                else:
                    sum = pfsum[j] - pfsum[i-1]
                all_sum.append(sum)
        all_sum = sorted(all_sum)
        # print(pfsum)
        # print(all_sum)
        max_sum = all_sum[0]
        if max_sum > B:
            return 0
        for i in range(len(all_sum)):
            if all_sum[i]<=B:
                max_sum = all_sum[i]
        return max_sum


print(Solution().maxSubarray(9,78,[ 7, 1, 8, 5, 8, 5, 3, 3, 5 ]))
print(Solution().maxSubarray(5,15, [2, 1, 3, 4, 5]))
print(Solution().maxSubarray(3,4, [1,2,3]))